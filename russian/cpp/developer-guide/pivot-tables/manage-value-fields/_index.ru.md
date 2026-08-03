---
title: Поля значений в Aspose.Cells for C++
linktitle: Поля значений в Aspose.Cells for C++
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for C++.
keywords: Aspose.Cells, C++, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ru/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует ваши исходные данные. Aspose.Cells предоставляет метод `PivotTable.AddFieldToArea(PivotFieldType, string)`, перегрузку, которая принимает константу `PivotFieldType.Data` и имя исходного столбца. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.DataFields` в порядке добавления полей. По умолчанию числовой исходный столбец агрегируется с помощью `ConsolidationFunction.Sum`, а для нечислового столбца по умолчанию используется `Count`.
## Изменение функции итогов
Каждое поле, помещённое в область данных, внутри оборачивается как экземпляр `PivotField`, и его свойство `Function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `Function` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.
{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, исходный столбец не меняется.
{{% /alert %}}
Таким образом, вы можете оставить одно поле данных как `Sum`, одновременно добавив второе поле данных, которое ссылается на тот же исходный столбец, но использует `Count` или `Average`, всё в одной сводной таблице.
## Размещение полей значений на оси строк или столбцов
Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле под названием `PivotTable.ValuesField`. Это виртуальное поле представляет агрегат каждого поля данных, находящегося в области данных. Вы можете перетащить его в область строк или столбцов как базовое поле сводной таблицы, что полезно для расположения нескольких мер рядом.
{{% alert color="primary" %}}
`PivotTable.ValuesField` не работает, если нет полей значений или есть только одно такое поле.
{{% /alert %}}
Приведённые ниже сценарии последовательно рассматривают три комплексных примера, демонстрирующих каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.
## Сценарий 1 — перетаскивание базового поля в область значений
Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После выполнения операции `Amount` появляется в области данных и вычисляется как `Sum` от `Amount` по умолчанию.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Aspose::Cells::Startup();

 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");

 Cells cells = worksheet.GetCells();

 // Заголовки в A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Строки данных A2:D9 с использованием вложенных циклов с разветвлением по j
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }

 // Добавить сводную таблицу в F3 с именем PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Макет сводной таблицы: Категория и Элемент в строках, Год в столбцах, Сумма как поле данных
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");

 Aspose::Cells::Cleanup();
 return 0;
}
```
## Сценарий 2 — изменение функции итогов
Этот сценарий начинается с той же структуры сводной таблицы, что и сценарий 1, но дважды добавляет поле `Amount` в область данных. Оба поля данных ссылаются на один и тот же исходный столбец, однако второе поле переопределяется с помощью сеттера `PivotField.Function`, так что оно становится `Count` вместо `Sum` по умолчанию.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Заполнить данные ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 PivotField countField = pivotTable.GetDataFields().Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```
## Сценарий 3 — размещение полей значений на оси строк или столбцов
При наличии двух полей данных `PivotTable.ValuesField` становится доступным для использования. Этот сценарий перетаскивает это агрегатное виртуальное поле в область столбцов, так что каждая мера в области данных отображается в виде отдельного столбцового блока рядом с `Year`.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... построить данные ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```
В совокупности эти три сценария охватывают все аспекты работы с полями значений в Aspose.Cells for C++ — от единственного поля данных с `Sum` по умолчанию до сводной таблицы с несколькими мерами, в которой виртуальное поле `ValuesField` управляет расположением на оси строк или столбцов.

{{< app/cells/assistant language="cpp" >}}
