---
title: Documents PDF sécurisés
type: docs
weight: 260
url: /fr/java/secure-pdf-documents/
description: Sécurisez les fichiers PDF lors de la conversion à partir de fichiers Excel. Cet article montre comment générer un fichier PDF sécurisé à partir d'Excel avec Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent travailler avec des fichiers PDF cryptés. Par exemple, ils doivent sécuriser les documents avec des mots de passe d'utilisateur et de propriétaire afin que n'importe qui ne puisse pas les ouvrir, ou souhaitent restreindre l'impression ou l'extraction du contenu du document.

Cet article explique comment transmettre les options de sécurité PDF lors de l'enregistrement de feuilles de calcul au format PDF.

{{% /alert %}} 

 Aspose.Cells Les API fournissent le[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)classe pour travailler avec la sécurité du format de fichier PDF. L'exemple de code ci-dessous décrit comment créer des fichiers PDF sécurisés avec Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
