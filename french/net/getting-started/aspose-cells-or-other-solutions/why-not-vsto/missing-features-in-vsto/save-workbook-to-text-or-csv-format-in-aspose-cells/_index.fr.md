---
title: Enregistrer le classeur au format Texte ou CSV dans Aspose.Cells
type: docs
weight: 110
url: /fr/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---

{{% alert color="primary" %}} 

Parfois, vous voulez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), à la fois Microsoft Excel et Aspose.Cells enregistrent par défaut le contenu de la feuille de calcul active uniquement.

{{% /alert %}} 

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, TxtSaveOptions.Separator est une virgule, donc ne spécifiez pas de séparateur lors de l'enregistrement au format CSV.

**C#**

{{< highlight csharp >}}

 string filePath = "source.xlsx";

//Load your source workbook

Workbook workbook = new Workbook(filePath);

//0-byte array

byte[] workbookData = new byte[0];

//Text save options. You can use any type of separator

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copy each worksheet data in text format inside workbook data array

for (int idx = 0; idx < workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
