---
title: Modifiez la police uniquement sur les caractères Unicode spécifiques lors de l'enregistrement au format PDF
type: docs
weight: 150
url: /fr/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}}

 Certains caractères Unicode ne peuvent pas être affichés par la police spécifiée par l'utilisateur. Un tel caractère Unicode est**Trait d'union insécable** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec**Times New Roman** , mais il peut être affiché avec d'autres polices comme**Arial Unicode MS**.

Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase qui se trouve dans une police spécifique comme Times New Roman, alors Aspose.Cells change la police du mot ou de la phrase entière en police qui pourrait afficher ce caractère comme Arial Unicode en MS.

Cependant, il s'agit d'un comportement indésirable pour certains utilisateurs et ils souhaitent uniquement que la police du caractère spécifique soit modifiée au lieu de modifier la police du mot ou de la phrase entière.

 Pour faire face à ce problème, le Aspose.Cells fournit[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propriété qui doit être définie**vrai**de sorte que seule la police du caractère spécifique qui n'est pas affichable est modifiée et que la police du reste du mot ou de la phrase reste la même.

{{% /alert %}}

## **Exemple**

 La capture d'écran suivante compare les deux PDF de sortie générés par l'exemple de code ci-dessous. Un a été généré sans réglage[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propriété et l'autre a été généré après avoir défini la[**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) propriété à**vrai**. Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière est passée de Times New Roman à Arial Unicode MS en raison du trait d'union insécable. Alors que dans le deuxième PDF, seule la police du trait d'union insécable a changé.

![tâche : image_autre_texte](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
