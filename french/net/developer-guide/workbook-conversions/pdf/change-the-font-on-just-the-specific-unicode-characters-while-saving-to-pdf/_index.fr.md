---
title: Modifiez la police uniquement sur les caractères Unicode spécifiques lors de l'enregistrement au format PDF
type: docs
weight: 260
url: /fr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Certains caractères Unicode ne peuvent pas être affichés par la police spécifiée par l'utilisateur. Un tel caractère Unicode est**Trait d'union insécable** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec**Times New Roman** , mais il peut être affiché avec d'autres polices comme**Arial Unicode MS**.

Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase qui se trouve dans une police spécifique comme Times New Roman, alors Aspose.Cells change la police du mot ou de la phrase entière en police qui pourrait afficher ce caractère comme Arial Unicode en MS.

Cependant, il s'agit d'un comportement indésirable pour certains utilisateurs et ils souhaitent que seule la police de ce caractère spécifique soit modifiée au lieu de modifier la police d'un mot ou d'une phrase entière.

Pour résoudre ce problème, Aspose.Cells fournit la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity qui doit être définie sur true afin que seule la police d'un caractère spécifique non affichable soit remplacée par une police affichable et que le reste du mot ou de la phrase reste dans la police d'origine.

{{% /alert %}} 
## **Exemple**
La capture d'écran suivante compare les deux PDF de sortie générés par l'exemple de code ci-dessous.

L'un est généré sans définir la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity et l'autre a été généré après avoir défini la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity sur true.

Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière est passée de Times New Roman à Arial Unicode MS en raison du trait d'union insécable. Alors que dans le deuxième Pdf, seule la police du trait d'union insécable a changé.

|**Premier fichier pdf**|
|:- |
|![tâche : image_autre_texte](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Deuxième fichier pdf**|
|:- |
|![tâche : image_autre_texte](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Exemple de code**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



