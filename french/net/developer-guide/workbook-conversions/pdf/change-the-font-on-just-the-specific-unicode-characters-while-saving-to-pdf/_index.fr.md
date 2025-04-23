---
title: Modifier la police uniquement des caractères Unicode spécifiques lors de l enregistrement en PDF
type: docs
weight: 260
url: /fr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Certains caractères Unicode ne peuvent pas être affichés par la police spécifiée par l'utilisateur. Un tel caractère Unicode est le **trait d'union insécable** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

Lorsqu'un tel caractère apparaît dans un mot ou une phrase en une police spécifique comme Times New Roman, alors Aspose.Cells change la police de tout le mot ou la phrase en une police qui pourrait afficher ce caractère comme Arial Unicode MS.

Cependant, ce comportement est indésirable pour certains utilisateurs et ils veulent uniquement que la police spécifique de ce caractère soit modifiée au lieu de changer la police de tout le mot ou la phrase.

Pour résoudre ce problème, Aspose.Cells fournit la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity qui doit être définie sur true afin que seule la police du caractère spécifique qui ne peut pas être affiché soit modifiée en une police affichable et le reste du mot ou de la phrase reste dans la police d'origine.

{{% /alert %}} 
## **Exemple**
La capture d'écran suivante compare les deux fichiers PDF générés par le code d'exemple ci-dessous.

L'un est généré sans définir la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity et l'autre a été généré après avoir défini la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity sur true.

Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière a été modifiée de Times New Roman à Arial Unicode MS en raison du tiret non sécable. Tandis que dans le deuxième PDF, seule la police du tiret non sécable a été modifiée.

|**Premier fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Deuxième fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Code d'exemple**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
