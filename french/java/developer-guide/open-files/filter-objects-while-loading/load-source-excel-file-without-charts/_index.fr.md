---
title: Charger le fichier Excel source sans graphiques
type: docs
weight: 750
url: /fr/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells vous permet de charger votre fichier Excel sans graphiques. Veuillez utiliser la propriété LoadOptions.LoadFilter à cet effet.

{{% /alert %}} 
## **Charger le fichier Excel source sans graphiques**
Le code d'exemple suivant charge le fichier Excel d'exemple sans graphiques et le sauvegarde au format PDF de sortie.





{{< highlight java >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






