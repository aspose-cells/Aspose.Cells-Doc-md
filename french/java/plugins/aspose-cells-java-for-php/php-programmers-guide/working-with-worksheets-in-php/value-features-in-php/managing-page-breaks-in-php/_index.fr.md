---
title: Gestion des sauts de page en PHP
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Gestion des sauts de page**
### **Ajouter des sauts de page**
 Pour ajouter des sauts de page à l'aide de**Aspose.Cells Java pour PHP** , appel**add_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code PHP**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Effacer tous les sauts de page**
 Pour effacer tous les sauts de page à l'aide de**Aspose.Cells Java pour PHP** , appel**clear_all_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code PHP**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Suppression d'un saut de page spécifique**
 Pour supprimer un saut de page spécifique à l'aide de**Aspose.Cells Java pour PHP** , appel**remove_page_break** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code PHP**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Gestion des sauts de page (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
