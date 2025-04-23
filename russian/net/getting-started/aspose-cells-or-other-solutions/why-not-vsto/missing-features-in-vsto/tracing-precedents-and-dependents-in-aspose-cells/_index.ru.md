---
title: Отслеживание предшествующих и зависимых ячеек в Aspose.Cells
type: docs
weight: 130
url: /ru/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Сложные финансовые рабочие листы, особенно те, которые разработаны в сотрудничестве, могут скрывать наиболее нелестные ошибки. Проверка формул на точность и поиск источника ошибки может быть сложной, когда формула использует предшествующие и зависимые ячейки.

- **Предшествующие ячейки** - это ячейки, на которые ссылается формула в другой ячейке. Например, если ячейка D10 содержит формулу =B5, то ячейка B5 является предшествующей по отношению к ячейке D10.
- **Зависимые ячейки** содержат формулы, которые относятся к другим ячейкам. Например, если ячейка D10 содержит формулу =B5, то ячейка D10 является зависимой от ячейки B5.

Чтобы сделать таблицу удобной для чтения, вы можете явно показать, какие ячейки в таблице используются в формулах. Точно так же, вы можете извлечь зависимые ячейки других ячеек.

Aspose.Cells позволяет отслеживать ячейки и выяснять, какие из них связаны между собой.

{{% /alert %}} 
## **Отслеживание предшествующих и зависимых ячеек: Microsoft Excel**
Формулы могут изменяться в зависимости от изменений, вносимых клиентом. Например, если ячейка C1 зависит от ячеек C3 и C4, содержащих формулы, и ячейка C1 изменена (таким образом, формула переопределена), то C3 и C4 или другие ячейки должны измениться для балансировки электронной таблицы в соответствии с бизнес-правилами.

Точно так же, допустим, что C1 содержит формулу "=(B1*22)/(M2*N32)". Я хочу найти ячейки, от которых зависит C1, то есть предшествующие ячейки B1, M2 и N32.

Вам может понадобиться отследить зависимость конкретной ячейки от других ячеек. Если бизнес-правила встроены в формулы, мы бы хотели выяснить зависимость и выполнить некоторые правила на ее основе. Точно так же, если значение конкретной ячейки изменено, какие ячейки в листе Excel будут затронуты этим изменением?

Microsoft Excel позволяет пользователям отслеживать предшественников и зависимых.

1. На **Панели инструментов Просмотр** выберите **Анализ формул**.
   Откроется диалоговое окно Анализ формул. 
   **Диалоговое окно аудита формул** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Следить за предшественниками:
   1. Выберите ячейку, содержащую формулу, для которой вы хотите найти предшествующие ячейки.
   1. Чтобы отобразить стрелку маршрута к каждой ячейке, которая непосредственно предоставляет данные для активной ячейки, щелкните **Отслеживание предшественников** на **Панели инструментов Проверка формул**.
1. Отследить формулы, которые ссылается на конкретную ячейку (зависимости)
   1. Введите ячейку, для которой вы хотите найти зависимые ячейки.
   1. Чтобы отобразить стрелку маршрута к каждой ячейке, которая зависит от активной ячейки, щелкните Отслеживание зависимости на панели инструментов Проверка формул.
## **Отслеживание предшественников и зависимых ячеек: Aspose.Cells**
### **Отслеживание предшественников**
Aspose.Cells облегчает получение предшествующих ячеек. Он может извлекать не только ячейки, предоставляющие данные для простых предшественников формул, но также находить ячейки, предоставляющие данные для сложных предшественников формул с именованными диапазонами.

В приведенном ниже примере используется шаблонный файл Excel, Book1.xls. На первом листе электронной таблицы содержатся данные и формулы.

**Входная электронная таблица** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells предоставляет метод GetPrecedents класса Cell, используемый для отслеживания предшественников ячейки. Он возвращает коллекцию ReferredAreaCollection. Как видите выше, в Book1.xls ячейка B7 содержит формулу "=SUM(A1:A3)". Таким образом, ячейки A1:A3 являются предшественниками для ячейки B7. Нижеприведенный пример демонстрирует функцию отслеживания предшественников с использованием файлового шаблона Book1.xls.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Отслеживание зависимых**
Aspose.Cells позволяет получить зависимые ячейки в электронных таблицах. Aspose.Cells может не только извлекать ячейки, предоставляющие данные по простой формуле, но и находить ячейки, предоставляющие данные сложным формулам с именованными диапазонами.

Aspose.Cells предоставляет метод GetDependents класса Cell, используемый для отслеживания зависимых ячеек. Например, в Book1.xlsx есть формулы: "=A1+20" и "=A1+30" в ячейках B2 и C2 соответственно. Нижеприведенный пример демонстрирует отслеживание зависимых для ячейки A1 с использованием файла-шаблона Book1.xlsx.

**C#**

{{< highlight csharp >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

{{< app/cells/assistant language="csharp" >}}
