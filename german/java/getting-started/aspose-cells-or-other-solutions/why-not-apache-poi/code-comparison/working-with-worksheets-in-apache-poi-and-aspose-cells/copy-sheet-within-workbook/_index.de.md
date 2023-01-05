---
title: Blatt innerhalb der Arbeitsmappe kopieren
type: docs
weight: 40
url: /de/java/copy-sheet-within-workbook/
---
## **Microsoft Excel – Verschieben oder Kopieren von Blättern innerhalb einer Arbeitsmappe**
Im Folgenden sind die Schritte zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen aufgeführt.

1. Um Blätter innerhalb oder zwischen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1.  Auf der**Bearbeiten** Menü, klicken**Blatt verschieben oder kopieren**.
1. Klicken Sie im Feld An Buch auf die Arbeitsmappe, um die Blätter zu erhalten.
1.  Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf**neues Buch**.
1.  Im**Vor Blatt** klicken Sie auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1.  Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie aus**Erstellen Sie eine Kopie** Kontrollkästchen.
## **Aspose.Cells - Blatt innerhalb der Arbeitsmappe kopieren**
{{% alert color="primary" %}} 

Aspose.Cells bietet eine überladene Methode, WorksheetCollection.addCopy(), die zum Hinzufügen eines Arbeitsblatts zur Sammlung und zum Kopieren von Daten aus einem vorhandenen Arbeitsblatt verwendet wird. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie Sie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopieren.

{{% /alert %}} 

Kopieren Sie Blätter mit Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS – Blatt innerhalb der Arbeitsmappe kopieren**
{{% alert color="primary" %}} 

Workbook.cloneSheet() wird verwendet, um Blätter mit Arbeitsmappe zu kopieren.

{{% /alert %}} 

Blätter mit Apache POI SS kopieren

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Kopieren und Verschieben von Arbeitsblättern](/cells/de/java/copying-and-moving-worksheets).

{{% /alert %}}
