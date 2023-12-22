---
title: Documents sécurisés PDF
type: docs
weight: 260
url: /fr/java/secure-pdf-documents/
description: Sécurisez les fichiers PDF lors de la conversion à partir de fichiers Excel. Cet article montre la génération d'un fichier sécurisé PDF à partir d'Excel avec Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent travailler avec des fichiers PDF cryptés. Par exemple:

- Sécurisez les documents avec les mots de passe du propriétaire et de l'utilisateur afin que n'importe qui puisse les ouvrir.
- Définissez des restrictions ou des autorisations sur le document après son ouverture. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment transmettre les options de sécurité PDF lors de l'enregistrement de feuilles de calcul dans PDF.

{{% /alert %}}

 Aspose.Cells fournit[**Options de sécurité Pdf**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement sous PDF. Le mot de passe propriétaire ou le mot de passe utilisateur sera requis pour ouvrir le document crypté PDF et le consulter.

- Le mot de passe de l'utilisateur peut être nul ou une chaîne vide, dans ce cas aucun mot de passe ne sera demandé à l'utilisateur lors de l'ouverture du document PDF.
- L'ouverture du document PDF avec le mot de passe propriétaire correct permet un accès complet (sans aucune restriction d'accès spécifiée) au document.
- L'ouverture du document PDF avec le mot de passe utilisateur correct (ou l'ouverture d'un document qui n'a pas de mot de passe utilisateur) permet un accès limité selon les autorisations spécifiées.

L'exemple de code ci-dessous décrit comment créer des fichiers PDF sécurisés avec Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[**Classeur.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()juste avant de le rendre dans PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
