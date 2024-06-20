---
title: Blatt innerhalb der Arbeitsmappe kopieren
type: docs
weight: 40
url: /de/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Verschieben oder Kopieren von Blättern innerhalb der Arbeitsmappe**
Im Folgenden sind die Schritte aufgeführt, die für das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen erforderlich sind.

1. Um Blätter innerhalb oder zwischen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Wählen Sie im Feld 'Zur Arbeitsmappe' die Arbeitsmappe aus, in die die Blätter eingefügt werden sollen.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf **Neue Arbeitsmappe**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter anstatt sie zu verschieben zu kopieren, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.
## **Aspose.Cells - Blatt innerhalb der Arbeitsmappe kopieren**
{{% alert color="primary" %}} 

Aspose.Cells bietet eine überladene Methode, WorksheetCollection.addCopy(), die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quell-Arbeitsblatts als Parameter. Die andere Version nimmt den Namen des Quell-Arbeitsblatts an.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{% /alert %}} 

Blätter mit Aspose.Cells kopieren

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Blatt innerhalb der Arbeitsmappe kopieren**
{{% alert color="primary" %}} 

Workbook.cloneSheet() wird verwendet, um Blätter in einer Arbeitsmappe zu kopieren.

{{% /alert %}} 

Blätter mit Apache POI SS kopieren

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Kopieren und Verschieben von Tabellenblättern](/cells/de/java/copying-and-moving-worksheets).

{{% /alert %}}
