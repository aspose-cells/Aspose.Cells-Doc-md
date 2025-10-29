---
title: Changer la police uniquement pour certains caractères Unicode lors de l enregistrement en PDF avec Golang via C++
linktitle: Modifier la police sur les caractères Unicode
type: docs
weight: 260
url: /fr/go-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Apprenez comment changer la police de caractères spécifiques Unicode lors de l enregistrement en PDF avec Aspose.Cells et Golang via C++.
---

{{% alert color="primary" %}}

Certains caractères Unicode ne sont pas affichables par la police spécifiée par l'utilisateur. Un de ces caractères Unicode est **Non-breaking Hyphen** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase en police spécifique comme Times New Roman, Aspose.Cells change la police de l'ensemble du mot ou de la phrase en une police pouvant afficher ce caractère comme Arial Unicode MS.

Cependant, ce comportement est indésirable pour certains utilisateurs, et ils souhaitent que seule la police de ce caractère spécifique soit modifiée au lieu de changer la police de tout le mot ou la phrase.

Pour résoudre ce problème, Aspose.Cells fournit la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity`, qui doit être réglée à `true` afin que seule la police du caractère spécifique qui ne peut pas être affiché soit modifiée en une police affichable, et le reste du mot ou de la phrase reste dans sa police d'origine.

{{% /alert %}}

## **Exemple**

La capture d'écran suivante compare les deux fichiers PDF générés par le code d'exemple ci-dessous.

Une est générée sans régler la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity`, et l'autre a été générée après avoir défini la propriété `PdfSaveOptions.IsFontSubstitutionCharGranularity` à `true`.

Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière a changé de Times New Roman à Arial Unicode MS à cause du tiret insécable. Alors que dans le deuxième PDF, seule la police du tiret insécable a changé.

|**Premier fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Second fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheFontOnJustTheSpecificUnicodeCharactersWhileSavingToPdf.go" >}}
