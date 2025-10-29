---
title: Vérifier si la signature numérique du code VBA est valide avec Golang via C++
linktitle: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Apprenez comment vérifier la validité d une signature numérique dans le code VBA en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/). Elle renverra **true** si la signature est valide ; sinon, elle renverra **false**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide en C++**

Le code suivant démontre l'utilisation de cette propriété avec le [fichier Excel d'exemple](5115030.xlsm) que vous pouvez télécharger via le lien fourni. Le même fichier Excel a une signature valide, mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis le revérifions, sa signature est devenue invalide.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
