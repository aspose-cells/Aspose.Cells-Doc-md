---
title: Speichern von Dateien
type: docs
weight: 20
url: /de/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells ermöglicht das Erstellen und Speichern von Dateien sowie das Bearbeiten vorhandener Dateien. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien gespeichert werden können.

{{% /alert %}} 
## **Verschiedene Möglichkeiten zum Speichern von Dateien**
 Aspose.Cells bietet die[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) die eine Microsoft Excel-Datei darstellt und Methoden bereitstellt, die zum Arbeiten mit Excel-Dateien erforderlich sind. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse bietet die[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Methode zum Speichern von Excel-Dateien. Das[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) -Methode verfügt über viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weise verwendet werden. Das Dateiformat, in dem die Datei gespeichert wird, wird von festgelegt[Format speichern](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)Aufzählung.
## **Datei an einem Ort speichern**
Um Dateien an einem Speicherort zu speichern, geben Sie den Dateinamen (komplett mit Speicherpfad) und das gewünschte Dateiformat (aus der[Format speichern](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) Aufzählung) beim Aufrufen der[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Objekt[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Datei im Stream speichern**
 Um Dateien in einem Stream zu speichern, erstellen Sie ein MemoryStream- oder FileStream-Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie die aufrufen[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Objekt[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Methode. Geben Sie das gewünschte Dateiformat mit an[Format speichern](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) Aufzählung beim Aufruf der[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
