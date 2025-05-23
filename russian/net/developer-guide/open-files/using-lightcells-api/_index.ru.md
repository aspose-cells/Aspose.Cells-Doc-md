---
title: Использование API LightCells
type: docs
weight: 160
url: /ru/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

Иногда вам необходимо читать и записывать большие файлы Microsoft Excel с огромным списком данных или контента на листе. API LightCells полезен для создания больших электронных таблиц Excel: благодаря этому, требуется меньше памяти, и достигается лучшая производительность и эффективность.

{{% /alert %}} 
# Архитектура, основанная на событиях
Aspose.Cells предоставляет API LightCells, преимущественно предназначенный для манипулирования данными ячейки одна за другой без построения полной модели данных (используя коллекцию Cell и т. д.) в памяти. Он работает в режиме событийного управления.

Для сохранения рабочих книг предоставьте содержание ячейки по ячейке при сохранении, и компонент сохранит его непосредственно в выходной файл.

При считывании файлов-шаблонов компонент анализирует каждую ячейку и предоставляет их значение по одной.

В обоих процедурах обрабатывается один объект ячейки, а затем он удаляется, объект Workbook не хранит коллекцию. В этом режиме, следовательно, память экономится при импорте и экспорте файлов Microsoft Excel с большим набором данных, который иначе использовал бы много памяти.

Несмотря на то, что API LightCells обрабатывает ячейки одинаково для файлов XLSX и XLS (он на самом деле не загружает все ячейки в память, а обрабатывает одну ячейку, а затем удаляет ее), он более эффективно экономит память для файлов XLSX, чем для файлов XLS из-за разных моделей данных и структур двух форматов.

Однако **для файлов XLS** для экономии памяти разработчики могут указать временное местоположение для сохранения временных данных, генерируемых в процессе сохранения. Обычно **использование API LightCells для сохранения файла XLSX может сэкономить 50% или более памяти** по сравнению с обычным способом, **сохранение XLS может сэкономить от 20 до 40% памяти**.
## Создание большого файла Excel
Aspose.Cells предоставляет интерфейс LightCellsDataProvider, который должен быть реализован в вашей программе. Интерфейс представляет поставщика данных для сохранения больших электронных таблиц в легком режиме.

При сохранении рабочей книги этим режимом каждый рабочий лист в рабочей книге проверяется при сохранении. Для одного листа, если StartSheet(int) равно true, то все данные и свойства строк и ячеек этого листа для сохранения предоставляются этой реализацией. В первую очередь вызывается NextRow(), чтобы получить индекс следующей строки для сохранения. Если возвращается допустимый индекс строки (индекс строки должен быть в порядке возрастания для сохранения строк), то предоставляется объект Row, представляющий эту строку, для установки ее свойств при StartRow(Row).

Для одной строки сначала проверяется NextCell(). Если возвращается допустимый индекс столбца (индекс столбца должен быть в порядке возрастания для всех ячеек одной строки для сохранения), то предоставляется объект Cell, представляющий эту ячейку, для установки ее данных и свойств при StartCell(Cell). После установки данных ячейки она непосредственно сохраняется в созданный файл электронной таблицы, и проверяется и обрабатывается следующая ячейка.
### Написание большого файла Excel: Пример
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.

Программа создает огромный файл с **10,000 (10000x30 матрица) записей** в листе Excel и заполняет их фиктивными данными. Вы можете указать свою матрицу, изменив переменные rowsCount и colsCount в методе Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Чтение больших файлов Excel
Aspose.Cells предоставляет интерфейс LightCellsDataHandler, который должен быть реализован в вашей программе. Этот интерфейс представляет поставщика данных для чтения больших файлов электронных таблиц в режиме сниженного веса.

При чтении книги в этом режиме StartSheet проверяется при чтении каждого листа в книге. Для листа, если StartSheet возвращает true, то все данные и свойства ячеек в строках и столбцах листа проверяются и обрабатываются реализацией этого интерфейса. Для каждой строки вызывается StartRow, чтобы проверить, нужно ли ее обрабатывать. Если строку нужно обработать, ее свойства считываются сначала, и разработчик может получить доступ к их свойствам с помощью ProcessRow. Если также нужно обрабатывать ячейки строки, то ProcessRow должен возвращать true, и затем для каждой существующей ячейки строки вызывается StartCell, чтобы проверить, нужно ли обрабатывать одну ячейку. Если нужно обрабатывать одну ячейку, вызывается ProcessCell для обработки ячейки реализацией этого интерфейса.
### Чтение больших файлов Excel: Пример
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.

Программа считывает огромный файл с миллионами записей в листе Excel. На чтение каждого листа в книге требуется небольшое время. Ознакомьтесь с образцовым кодом чтения файла и получения общего количества ячеек, количества строк и формул в каждом листе.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
