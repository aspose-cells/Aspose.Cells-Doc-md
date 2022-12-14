---
title: Prise en charge de la mise en page des balises DIV lors du chargement de HTML dans un classeur Excel
type: docs
weight: 50
url: /fr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---
{{% alert color="primary" %}} 

Normalement, la disposition des balises div est ignorée lors du chargement de HTML dans un objet de classeur Excel. Toutefois, si vous souhaitez que la disposition des balises div ne soit pas ignorée, veuillez définir le[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) propriété à**vrai** . La valeur par défaut de cette propriété est**faux**.

{{% /alert %}} 

 L'exemple de code suivant illustre l'utilisation de[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) propriété. Veuillez télécharger le[Aspose Logo](5115218.png) utilisé dans le code HTML d'entrée et le[fichier excel de sortie](5115220.xlsx) généré par le code.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
