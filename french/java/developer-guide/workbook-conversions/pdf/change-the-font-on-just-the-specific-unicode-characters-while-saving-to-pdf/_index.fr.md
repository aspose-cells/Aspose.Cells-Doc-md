---
title: Modifier la police uniquement des caractères Unicode spécifiques lors de l enregistrement en PDF
type: docs
weight: 150
url: /fr/java/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}}

Certains caractères Unicode ne sont pas affichables par la police spécifiée par l'utilisateur. Un de ces caractères Unicode est **Non-breaking Hyphen** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase qui est dans une police spécifique comme Times New Roman, alors Aspose.Cells change la police de tout le mot ou de la phrase à une police qui pourrait afficher ce caractère comme Arial Unicode MS.

Cependant, ce comportement est indésirable pour certains utilisateurs et ils veulent seulement que la police du caractère spécifique soit modifiée au lieu de changer la police de tout le mot ou de la phrase.

Pour résoudre ce problème, Aspose.Cells fournit la propriété [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) qui doit être définie sur **true** afin que seule la police du caractère spécifique qui n'est pas affichable soit modifiée et que la police pour le reste du mot ou de la phrase reste la même.

{{% /alert %}}

## **Exemple**

La capture d'écran suivante compare les deux PDF générés par le code d'exemple ci-dessous. L'un a été généré sans définir la propriété [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) et l'autre a été généré après avoir défini la propriété [**PdfSaveOptions.setFontSubstitutionCharGranularity()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IsFontSubstitutionCharGranularity) sur **true**. Comme vous pouvez le voir dans le premier PDF, la police de toute la phrase a changé de Times New Roman à Arial Unicode MS à cause du Non-Breaking Hyphen. Alors que dans le deuxième PDF, seule la police du Non-Breaking Hyphen a changé.

![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeFontonspecificUnicodecharacters-ChangeFontonspecificUnicodecharacters.java" >}}
{{< app/cells/assistant language="java" >}}
