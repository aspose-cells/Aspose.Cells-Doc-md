---
title: Vérifier le mot de passe des fichiers chiffrés
type: docs
weight: 10
url: /fr/net/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifiez le mot de passe des fichiers Excel chiffrés (xlsx, xlsb, xls, xlsm) et des fichiers Open Office (ODS) à l aide de codes CShape.
---

{{% alert color="primary" %}}
Si les fichiers Excel (xlsx, xlsb, xls, xlsm) et Open Office (ODS) sont verrouillés par un mot de passe, Aspose prend en charge une vérification simple du mot de passe sans analyser des données spécifiques des fichiers.
{{% /alert %}}

## **Vérifiez le mot de passe du fichier chiffré**

Pour vérifier le mot de passe du fichier chiffré, Aspose.Cells for .NET propose la méthode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Ces méthodes acceptent deux paramètres, le flux de fichiers et le mot de passe qui doit être vérifié.
Le code d'exemple suivant démontre l'utilisation de la méthode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) pour vérifier si le mot de passe fourni est valide ou non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

