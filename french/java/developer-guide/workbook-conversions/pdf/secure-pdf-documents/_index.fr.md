---
title: Documents PDF sécurisés
type: docs
weight: 260
url: /fr/java/secure-pdf-documents/
description: Sécurisez les fichiers PDF lors de la conversion à partir de fichiers Excel. Cet article démontre la génération de fichiers PDF sécurisés à partir d Excel avec l API Aspose.Cells for Java.
keywords: documents pdf sécurisés java, documents pdf sécurisés, excel en pdf sécurisé, excel en pdf sécurisé java, convertir excel en pdf sécurisé, convertir excel en pdf sécurisé java, convertir excel en pdf protégé par mot de passe, convertir excel en pdf protégé par mot de passe java, excel en pdf protégé par mot de passe java, excel en pdf protégé par mot de passe
---

{{% alert color="primary" %}}

Parfois, les développeurs ont besoin de travailler avec des fichiers PDF cryptés. Par exemple :

- Sécuriser les documents avec des mots de passe propriétaire et utilisateur afin que n'importe qui ne puisse pas l'ouvrir.
- Définir des restrictions ou des autorisations sur le document après l'ouverture du document. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment passer des options de sécurité PDF lors de l'enregistrement des feuilles de calcul au format PDF.

{{% /alert %}}

Aspose.Cells fournit [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement au format PDF. Le mot de passe propriétaire ou le mot de passe utilisateur sera nécessaire pour ouvrir le document PDF crypté pour visualisation.

- Le mot de passe utilisateur peut être nul ou une chaîne vide, dans ce cas aucun mot de passe ne sera requis de la part de l'utilisateur lors de l'ouverture du document PDF.
- Ouvrir le document PDF avec le bon mot de passe propriétaire permet un accès complet (sans aucune restriction d'accès spécifiée) au document.
- Ouvrir le document PDF avec le bon mot de passe utilisateur (ou ouvrir un document qui n'a pas de mot de passe utilisateur) permet un accès limité comme les autorisations spécifiées.

Le code d'exemple ci-dessous décrit comment créer des fichiers PDF sécurisés avec l'API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Si le tableur contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
