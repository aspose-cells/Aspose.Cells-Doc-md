---
title: Gestion des sauts de page en Php
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Gérer les sauts de page**
### **Ajout de sauts de page**
Pour ajouter des sauts de page avec **Aspose.Cells Java pour PHP**, appelez la méthode **add_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Effacement de tous les sauts de page**
Pour effacer tous les sauts de page avec **Aspose.Cells Java pour PHP**, appelez la méthode **clear_all_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code PHP**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Supprimer un saut de page spécifique**
Pour supprimer un saut de page spécifique avec **Aspose.Cells Java pour PHP**, appelez la méthode **remove_page_break** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Gestion des sauts de page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
