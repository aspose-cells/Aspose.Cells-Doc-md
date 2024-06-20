---
title: Convertir le classeur en HTML à l aide d Aspose.Cells
type: docs
weight: 20
url: /fr/java/convert-workbook-to-html-using-aspose-cells/
---

## **Aspose.Cells - Convertir le classeur en HTML**
Les API Aspose.Cells prennent en charge l'exportation de feuilles de calcul au format HTML. À cette fin, **Aspose.Cells** utilise la classe **HtmlSaveOptions** qui permet aux développeurs de contrôler plusieurs aspects du HTML de sortie.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Convertir des fichiers Excel en HTML](/cells/fr/java/converting-workbook-to-different-formats/).

{{% /alert %}}
