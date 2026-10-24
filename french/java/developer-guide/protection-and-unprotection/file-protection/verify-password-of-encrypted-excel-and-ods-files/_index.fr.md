---
title: Vérifier le mot de passe des fichiers chiffrés
type: docs
weight: 10
url: /fr/java/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifier le mot de passe des fichiers Excel (xlsx, xlsb, xls, xlsm) et OpenOffice (ODS) cryptés à l aide de codes Java.
---

{{% alert color="primary" %}}
Si des fichiers Excel (xlsx, xlsb, xls, xlsm) et OpenOffice (ODS) sont verrouillés par un mot de passe, Aspose.Cells for Java prend en charge la vérification simple du mot de passe sans analyser des données spécifiques des fichiers.
{{% /alert %}}

## **Vérifiez le mot de passe du fichier chiffré**

Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for Java fournit la méthode [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-). Les méthodes acceptent deux paramètres, le flux de fichier et le mot de passe à vérifier.
Le code d'exemple suivant démontre l'utilisation de la méthode [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) pour vérifier si le mot de passe fourni est valide ou non.

### **Code exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
