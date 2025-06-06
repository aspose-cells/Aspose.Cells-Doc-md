---  
title: Установка динамических массивных формул с помощью Node.js через C++  
linktitle: Установка динамических массивных формул  
description: Как использовать библиотеку Aspose.Cells для вычисления динамических массивных формул в Excel с помощью Node.js через C++. Легко загружайте, вычисляйте и сохраняйте файлы Excel.  
keywords: Динамические массивные формулы, динамические массивные формулы в Excel, установка динамических массивных формул Node.js через C++, вычисление динамических массивных формул Node.js через C++, управление динамическими массивными формулами Excel.  
type: docs  
weight: 70  
url: /ru/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **Что такое массивная формула Excel**  
В Excel массивная формула - это специальный тип формулы, который позволяет выполнять вычисления над массивами данных, а не отдельными ячейками. Массивные формулы могут использоваться для выполнения сложных вычислений, манипулирования данными и эффективного решения конкретных проблем. Они вводятся по-другому, чем обычные формулы, и часто требуют использования Ctrl + Shift + Enter.

Вот несколько ключевых моментов о массивных формулах в Excel:  
1. Синтаксис:  
<br>  
Массивные формулы записываются как обычные формулы, но включают операции над массивами значений. Они заключены в фигурные скобки { }, чтобы указать, что это массивные формулы. Однако вы сами не вводите эти фигурные скобки; Excel автоматически добавляет их, когда вы вводите формулу правильно.  
2. Ввод массивных формул:  
<br>  
Чтобы ввести массивную формулу, введите её в строку формулы. Вместо нажатия Enter для завершения, нажмите Ctrl + Shift + Enter. Это сообщает Excel, что это массивная формула. Когда введена правильно, Excel отображает формулу в фигурных скобках в строке формул, указывая, что это массивная формула.  
3. Случаи использования:  
<br>  
Массивные формулы полезны для выполнения вычислений по нескольким ячейкам или диапазонам одновременно. Они могут использоваться для выполнения сложных математических вычислений, условных операций, фильтрации данных и многого другого.  
4. Преимущества:  
<br>  
Массивные формулы позволяют выполнить сложные вычисления в одной формуле, что может улучшить эффективность и упростить ваши рабочие листы. Они могут обрабатывать большие наборы данных и выполнять вычисления, которые в противном случае требовали бы нескольких промежуточных этапов.  
5. Ограничения:  
<br>  
Массивные формулы могут быть сложнее понять и устранить неисправности, чем обычные формулы. Они могут замедлить производительность рабочего листа, особенно если используются обширно или с большими наборами данных.  
6. Примеры:  
<br>  
Суммирование значений в диапазоне: **{=SUM(A1:A5*B1:B5)}**  
<br>  
Поиск максимального значения в диапазоне: **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Помните, что массивные формулы следует использовать осмотрительно, и важно понимать, как они работают, прежде чем применять их в ваших рабочих книгах. Они могут быть мощным инструментом для анализа данных и манипулирования в Excel.

## **Что такое динамическая массивная формула Excel**  
Динамические массивные формулы - новая функция, введенная в Excel 365 и Excel 2021. Они позволяют работать с массивами данных более плавно и эффективно по сравнению с традиционными массивными формулами. Динамические массивные формулы автоматически распространяют результаты на соседние ячейки, устраняя необходимость в Ctrl + Shift + Enter и облегчая манипуляцию данными.

Основные моменты динамических массивных формул в Excel:  
1. Автоматическое распространение:  
<br>  
Динамические массивные формулы автоматически распространяют результаты в соседние ячейки в зависимости от размера выходных данных. Это означает, что вам не нужно выбирать диапазон ячеек перед вводом формулы или использовать Ctrl + Shift + Enter для подтверждения формулы.  
2. Ввод в одну ячейку:  
<br>  
Динамические массивные формулы вводятся в одной ячейке, и Excel автоматически заполняет соседние ячейки результатами. Это упрощает управление и понимание формул, поскольку вам нужно ввести формулу только один раз.  
3. Новые функции:  
<br>  
Динамические массивные формулы представляют новые функции, которые могут обрабатывать массивы нативно, такие как **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** и **RANDARRAY**. Эти функции могут возвращать несколько значений или напрямую манипулировать массивами, упрощая сложные вычисления.  
4. Гибкая обработка диапазонов:  
<br>  
Динамические массивные формулы автоматически изменяют размер затопляемого диапазона динамически в зависимости от размера входных данных или выполняемых вычислений. Эта гибкость позволяет более эффективно использовать рабочее пространство и упрощает создание формул.  
5. Повышенная производительность:  
<br>  
Динамические массивные формулы могут улучшить производительность по сравнению с традиционными массивными формулами, особенно при работе с большими наборами данных или сложными вычислениями.  
6. Совместимость:  
<br>  
Динамические массивные формулы доступны в Excel 365 и Excel 2021. В старых версиях Excel они могут не поддерживаться.  
7. Примеры динамических массивных формул:  
<br>  
**FILTER**: Возвращает массив значений, которые соответствуют указанным критериям.  
<br>  
**SORT**: Сортирует значения в диапазоне или массиве.  
<br>  
**УНИКАЛЬНЫЙ**: Возвращает уникальные значения из списка или диапазона.  
<br>  
**ПОСЛЕДОВАТЕЛЬНОСТЬ**: Генерирует последовательность чисел или дат.  
<br>  
**RANDARRAY**: Генерирует массив случайных чисел.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Динамические массивные формулы предлагают мощные возможности для манипулирования и анализа данных в Excel, что облегчает работу с массивами данных и эффективно выполняет сложные вычисления.

## **В чем разница между массивными формулами и динамическими массивными формулами в Excel**  
В Excel как массивные, так и динамические массивные формулы используются для выполнения вычислений над несколькими значениями одновременно, но у них есть некоторые различия в функциональности и способе их реализации.

### **Черты массивных формул**  
1. Массивные формулы - это традиционные формулы в Excel, которые могут выполнять вычисления над массивами данных.  
2. Они вводятся нажатием Ctrl + Shift + Enter после набора формулы, что сообщает Excel, что это массивная формула.  
3. Массивные формулы имеют ограничения по способности выводить результаты в соседние ячейки. Обычно они возвращают один результат, хотя этот результат может быть массивом ячеек.  
4. Они существуют уже давно и поддерживаются во всех версиях Excel.

### **Черты динамическиx массивных формул**  
1. Динамические массивные формулы - новая функция, введенная в Excel 365 (подписка Office 365) и Excel 2021.  
2. Они автоматически выводят результаты в соседние ячейки в зависимости от размера входных данных или вычислений формулы.  
3. Динамические массивные формулы не требуют нажатия Ctrl + Shift + Enter; достаточно ввести формулу в одну ячейку, и Excel автоматически заполнит соседние ячейки результатами.  
4. Эти формулы могут возвращать несколько результатов (диапазон ячеек) напрямую без необходимости использования массивной формулы или Ctrl + Shift + Enter.  
5. У них есть новые функции, такие как **FILTER**, **SORT**, **UNIQUE** и другие, которые могут работать с массивами нативно и возвращать результаты в формате динамического массива.  
В заключение, динамические массивные формулы являются более современным и удобным способом работы с массивами в Excel, обеспечивая автоматическое разливание результатов и упрощая процесс работы с массивами по сравнению с традиционными массивными формулами. Однако они доступны только в более новых версиях Excel, поддерживающих динамические массивы.

## **Как настроить и вычислить динамические массивные формулы в Excel**  
Настройка динамических массивных формул в Excel включает использование конкретных функций, предназначенных для работы с массивами данных и позволяющих результатам автоматически разливаться в соседние ячейки. 

Вот пошаговое руководство по настройке динамических формул массива:  
1. Выберите ячейку:  
<br>  
Выберите ячейку, в которой вы хотите увидеть результаты динамической формулы массива. Динамические формулы массива выливают результаты в смежные ячейки, поэтому убедитесь, что для выливаемого вывода достаточно места.  
2. Введите формулу:  
<br>  
Введите динамическую формулу массива в строке формул выбранной ячейки. Используйте одну из доступных функций динамического массива в Excel 365 и Excel 2021, таких как **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY**, или **RANDARRAY**.  
<br>  
Например, вы можете использовать функцию FILTER для фильтрации списка данных на основе конкретных критериев: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Нажмите Enter:  
<br>  
После ввода формулы просто нажмите Enter на клавиатуре. В отличие от традиционных массивных формул, вам не нужно нажимать Ctrl + Shift + Enter.  
4. Обратите внимание на расширяемый диапазон:  
<br>  
Excel автоматически выливает результаты формулы в смежные ячейки. Выливаемый диапазон динамически корректируется в зависимости от размера выходных данных или вычислений, выполненных формулой. Excel выделяет выливаемый диапазон рамкой и значком диагональной стрелки, чтобы указать, что он содержит выливаемые данные.  
5. Взаимодействуйте с расширяемым диапазоном:  
<br>  
Вы можете взаимодействовать с выливаемым диапазоном так же, как с любым другим диапазоном ячеек в Excel. Используйте выливаемый диапазон в других формулах, выполняйте вычисления, форматируйте его или ссылайтесь на него в графиках или таблицах.  
6. Обновите формулу:  
<br>  
Если необходимо изменить динамическую массивную формулу, просто отредактируйте ее в исходной ячейке, где она была введена. После редактирования нажмите Enter снова для подтверждения изменений. Excel автоматически обновит расширяемый диапазон при необходимости.  
7. Очистка расширяемого диапазона:  
<br>  
Если вы хотите очистить выливаемые данные, вы можете удалить формулу из изначальной ячейки. Excel также очистит выливаемый диапазон. В качестве альтернативы вы можете удалить выливаемый диапазон непосредственно, выбрав его и нажав клавишу Delete.  
<br>  

Следуя этим шагам, вы можете настроить динамические формулы массива в Excel для эффективного анализа и манипуляции массивами данных, что облегчит анализ данных и задачи отчетности.

## **Как настроить и обновить динамические формулы массива с помощью Aspose.Cells**  
Пожалуйста, посмотрите следующий пример кода, который загружает [пример файла Excel](dynamicArrayFormula.xlsx), содержащий некоторые фиктивные данные. После загрузки файла вызовите функцию [Cell.setDynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setDynamicArrayFormula-string-formulaparseoptions-boolean-) для установки динамической массивной формулы и [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/nodejs-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) для обновления динамических массивных формул перед вызовом вычисления формулы, в конечном итоге сохраните книгу как [выходной файл Excel](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

Снимок вывода:  
<br>  
<image src="4.png" width="70%" />  

