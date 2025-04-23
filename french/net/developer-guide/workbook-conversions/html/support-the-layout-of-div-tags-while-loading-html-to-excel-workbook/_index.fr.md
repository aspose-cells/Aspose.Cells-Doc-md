---
title: Prise en charge de la disposition des balises DIV lors du chargement de HTML dans le classeur Excel
type: docs
weight: 50
url: /fr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalement, la disposition des balises div est ignorée lors du chargement HTML dans un objet classeur Excel. Cependant, si vous ne voulez pas que la disposition des balises div soit ignorée, veuillez définir la propriété [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) sur **true**. La valeur par défaut de cette propriété est **false**.

{{% /alert %}} 

Le code d'exemple suivant illustre l'utilisation de la propriété [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag). Veuillez télécharger le [logo Aspose](5115218.png) utilisé dans le HTML d'entrée et le [fichier Excel de sortie](5115220.xlsx) généré par le code.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
