---
title: Dateien speichern
type: docs
weight: 20
url: /de/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells ermöglicht das Erstellen und Speichern von Dateien sowie das Bearbeiten bestehender Dateien. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien gespeichert werden können.

{{% /alert %}} 
##  **Verschiedene Möglichkeiten zum Speichern von Dateien**
 Aspose.Cells bietet die[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Dies stellt eine Microsoft Excel-Datei dar und stellt die für die Arbeit mit Excel-Dateien erforderlichen Methoden bereit. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse bietet die[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode zum Speichern von Excel-Dateien. Der[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Die Methode verfügt über viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weise verwendet werden. Das Dateiformat, in dem die Datei gespeichert wird, wird von bestimmt[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)Aufzählung.
##  **Datei an einem Ort speichern**
Um Dateien an einem Speicherort zu speichern, geben Sie den Dateinamen (komplett mit Speicherpfad) und das gewünschte Dateiformat (aus der Datei) an[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung) beim Aufruf der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Datei im Stream speichern**
 Um Dateien in einem Stream zu speichern, erstellen Sie ein MemoryStream- oder FileStream-Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie Folgendes aufrufen[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Geben Sie das gewünschte Dateiformat mit an[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Aufzählung beim Aufruf der[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
