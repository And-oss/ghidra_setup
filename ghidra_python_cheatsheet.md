# Шпаргалка по созданию скриптов для Ghidra на Python

## 1. Основы
- **Язык**: Python (Jython)
- **Путь для скриптов**: `ghidra_scripts` в каталоге пользователя
- **Запуск скрипта**: `Window -> Script Manager -> Refresh -> Run`
- **Создание нового скрипта**: `Script Manager -> New Script`
- **Использование API**: Ghidra предоставляет мощное API для анализа бинарных файлов.

## 2. Базовый шаблон скрипта
Каждый скрипт в Ghidra должен использовать глобальные переменные, предоставляемые средой выполнения.
```python
from ghidra.program.model.listing import *
from ghidra.program.model.symbol import *

def run():
    print("Hello from Ghidra Script!")
```

## 3. Доступ к функциям и инструкциям
### Получение списка функций с адресами и размерами
```python
functionManager = currentProgram.getFunctionManager()
for function in functionManager.getFunctions(True):
    print(f"Function: {function.getName()} at {function.getEntryPoint()} (size: {function.getBody().getNumAddresses()} bytes)")
```

### Получение всех инструкций с адресами и их операндами
```python
listing = currentProgram.getListing()
instr_iter = listing.getInstructions(True)
for instr in instr_iter:
    print(f"{instr.getAddress()}: {instr} Operands: {instr.getOpObjects()}")
```

## 4. Работа с памятью
### Чтение байтов из памяти
```python
memory = currentProgram.getMemory()
start = currentProgram.getMinAddress()
data = memory.getBytes(start, 16)
print("Data:", data.hex())
```

### Запись байтов в память
```python
memory.setByte(currentAddress, 0x90)  # Запись NOP (0x90)
```

## 5. Метки и символы
### Создание и поиск метки
```python
symTable = currentProgram.getSymbolTable()
symTable.createLabel(currentAddress, "MyLabel", currentProgram.getGlobalNamespace(), SourceType.USER_DEFINED)
```
```python
symbol = symTable.getSymbols("MyLabel")
for sym in symbol:
    print(f"Symbol {sym.getName()} at {sym.getAddress()}")
```

## 6. Работа с комментариями
### Добавление комментария к адресу
```python
listing = currentProgram.getListing()
codeUnit = listing.getCodeUnitAt(currentAddress)
codeUnit.setComment(CodeUnit.PLATE_COMMENT, "Это комментарий для анализа")
```

## 7. Поиск строк в бинаре
```python
from ghidra.program.model.mem import *
memory = currentProgram.getMemory()
addr = currentProgram.getMinAddress()
while addr < currentProgram.getMaxAddress():
    data = memory.getBytes(addr, 64)
    try:
        text = data.decode("utf-8")
        if any(c.isprintable() for c in text):
            print(f"Found string at {addr}: {text}")
    except UnicodeDecodeError:
        pass
    addr = addr.add(64)
```

## 8. Работа с дизассемблером
```python
disassembler = currentProgram.getListing().getInstructionAt(currentAddress)
if disassembler:
    print(disassembler)
```

## 9. Поиск функций без имен
```python
functionManager = currentProgram.getFunctionManager()
for function in functionManager.getFunctions(True):
    if function.getName().startswith("FUN_"):
        print(f"Unnamed function at {function.getEntryPoint()}")
```

## 10. Обход всех байтов бинаря
```python
memory = currentProgram.getMemory()
addr = currentProgram.getMinAddress()
while addr < currentProgram.getMaxAddress():
    byte = memory.getByte(addr)
    print(f"{addr}: {byte:02X}")
    addr = addr.add(1)
```

## 11. Взаимодействие с пользователем
### Запрос строки
```python
user_input = askString("Input Required", "Enter a value:")
print(f"User entered: {user_input}")
```

### Запрос выбора из списка
```python
options = ["Option 1", "Option 2", "Option 3"]
choice = askChoice("Select Option", "Choose one:", options, options[0])
print(f"Selected: {choice}")
```

## 12. Обработка ошибок и контроль выполнения
```python
from ghidra.util.task import TaskMonitor
monitor = TaskMonitor.DUMMY

def do_something():
    if monitor.isCancelled():
        return
    print("Task running...")
do_something()
```

## 13. Завершение работы и сохранение изменений
```python
currentProgram.flushEvents()
print("Changes saved.")
```
