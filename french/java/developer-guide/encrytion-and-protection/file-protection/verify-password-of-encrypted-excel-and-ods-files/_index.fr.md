---
title: Vérifier le mot de passe des fichiers cryptés
type: docs
weight: 10
url: /fr/java/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifiez le mot de passe des fichiers chiffrés Excel (xlsx, xlsb, xls, xlsm) et Open office (ODS) à l'aide des codes Java.
---
{{% alert color="primary" %}}
Si les fichiers Excel (xlsx, xlsb, xls, xlsm) et Open office (ODS) sont verrouillés avec un mot de passe, Aspose.Cells for Java prend en charge la vérification simple du mot de passe sans analyser les données spécifiques des fichiers.
{{% /alert %}}

## **Vérifier le mot de passe du fichier crypté**

 Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for Java fournit le[**Vérifier le mot de passe**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)méthode. Les méthodes acceptent deux paramètres, le flux de fichiers et le mot de passe qui doit être vérifié.
 L'extrait de code suivant illustre l'utilisation de[**Vérifier le mot de passe**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) pour vérifier si le mot de passe fourni est valide ou non.

### **Exemple de code :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

