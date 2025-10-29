---
title: Imprimer et prévisualiser le classeur
linktitle: Imprimer et prévisualiser
type: docs
weight: 70
url: /fr/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells pour Python via .NET prend en charge l impression et l aperçu avant impression des fichiers Excel sans installation de Microsoft Excel.
---

{{% alert color="primary" %}}

Après avoir créé une feuille de calcul, vous souhaitez souvent en imprimer une copie papier. Cet article explique comment imprimer des feuilles de calcul avec Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Introduction à l'impression**

Microsoft Excel suppose que vous souhaitez imprimer toute la zone de la feuille à moins que vous ne spécifiiez une sélection. Pour imprimer avec Aspose.Cells pour Python via .NET, importez d'abord l'espace de noms aspose.cells.rendering dans le programme. Il possède plusieurs classes utiles, par exemple, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) et [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Impression à l'aide de SheetRender**

La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) représente une feuille de calcul et possède la méthode [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) qui peut imprimer une feuille de calcul. Le code d'exemple suivant montre comment imprimer une feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Impression à l'aide de WorkbookRender**

Pour imprimer un classeur entier, itérez à travers les feuilles et imprimez-les, ou utilisez la classe [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET offre également des surcharge pour les méthodes [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) et [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), il est donc possible de définir le nom du travail d'impression lors de l'impression de feuilles Excel. Par défaut, tous les travaux d'impression sont créés avec le nom "Document".

{{% /alert %}}

## **Aperçu avant impression**

Il peut arriver que des fichiers Excel comportant des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans de tels cas, la fonction Aperçu avant impression du classeur et de la feuille de calcul pourrait s'avérer utile. Avant de convertir de tels fichiers, l'utilisateur peut vérifier le nombre total de pages et décider ensuite de les convertir ou non. Cet article met l'accent sur l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) pour déterminer le nombre total de pages.

Aspose.Cells pour Python via .NET fournit la fonction d'aperçu avant impression. Pour cela, l'API fournit les classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview). Pour créer l'aperçu avant impression de l'ensemble du classeur, créez une instance de la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) en passant les objets [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) au constructeur. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) offre une méthode [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) qui renvoie le nombre de pages dans l'aperçu généré. Semblable à la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) est utilisée pour générer un aperçu avant impression pour une feuille spécifique. Pour créer un aperçu d'impression d'une feuille, créez une instance de la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) en passant [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) à son constructeur. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) fournit également une méthode [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/) qui renvoie le nombre de pages dans l'aperçu généré.

Le code suivant montre l'utilisation à la fois des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) en utilisant le [fichier Excel d'exemple](94896177.xlsx).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Voici la sortie générée en exécutant le code ci-dessus.

### **Sortie console**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
