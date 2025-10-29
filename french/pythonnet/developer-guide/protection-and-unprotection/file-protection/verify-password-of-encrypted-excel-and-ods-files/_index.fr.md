---
title: Vérifier le mot de passe des fichiers chiffrés
type: docs
weight: 10
url: /fr/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifiez le mot de passe des fichiers Excel chiffrés (xlsx, xlsb, xls, xlsm) et des fichiers Open Office (ODS) à l aide de codes CShape.
---

{{% alert color="primary" %}}
Si les fichiers Excel (xlsx, xlsb, xls, xlsm) et Open Office (ODS) sont verrouillés par un mot de passe, Aspose prend en charge une vérification simple du mot de passe sans analyser des données spécifiques des fichiers.
{{% /alert %}}

## **Vérifiez le mot de passe du fichier chiffré**

Pour vérifier le mot de passe du fichier chiffré, Aspose.Cells pour Python via .NET fournit la méthode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Ces méthodes acceptent deux paramètres, le flux de fichier et le mot de passe à vérifier.
Le code d'exemple suivant démontre l'utilisation de la méthode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) pour vérifier si le mot de passe fourni est valide ou non.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


{{< app/cells/assistant language="python-net" >}}
