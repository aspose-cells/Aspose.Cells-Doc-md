---
title: Détecter le type d hyperlien avec Golang via C++
linktitle: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/go-cpp/detect-hyperlink-type/
description: Apprenez à détecter le type de lien hypertexte via l API Aspose.Cells for C++.
keywords: Détecter le type d hyperlien, Détecter le type d hyperlien, Obtenir le type d hyperlien
---

## **Détecter le type de lien hypertexte**

Un fichier Excel peut comporter différents types d'hyperliens tels que des liens externes, des références de cellules, des chemins de fichiers, etc. Aspose.Cells prend en charge la fonctionnalité de détection du type d'hyperlien. Les types d'hyperliens sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) comporte les membres suivants.

- Externe : Lien externe
- Chemin de fichier : Chemin local et complet vers les fichiers/dossiers.
- E-mail : E-mail
- Référence de cellule : Lien vers une cellule ou une plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) fournit une propriété [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) avec un type de retour de [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). L'extrait de code suivant montre l'utilisation de la propriété [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Ce qui suit est le résultat généré par le code donné ci-dessus.

### Sortie de la Console
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
