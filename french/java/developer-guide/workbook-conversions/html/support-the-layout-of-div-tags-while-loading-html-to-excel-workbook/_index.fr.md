---
title: Prise en charge de la disposition des balises DIV lors du chargement de HTML dans le classeur Excel
type: docs
weight: 770
url: /fr/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalement, la mise en page des balises div est ignorée lors du chargement d'HTML dans un objet classeur Excel. Cependant, si vous souhaitez que la mise en page des balises div ne soit pas ignorée, veuillez définir la propriété [HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag) sur **true**. La valeur par défaut de cette propriété est **false**.

{{% /alert %}} 
## **Prise en charge de la mise en page des balises DIV lors du chargement d'HTML dans le classeur Excel**
Le code d'exemple suivant illustre l'utilisation de la propriété [HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag). Veuillez télécharger le Logo Aspose (5473442.png) utilisé à l'intérieur de l'HTML d'entrée et le fichier excel de sortie (5473439.xlsx) généré par le code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-SupportthelayoutofDIVtags-1.java" >}}
{{< app/cells/assistant language="java" >}}
