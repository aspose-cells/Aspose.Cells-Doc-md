---
title: Implémenter le système de date 1904 avec Golang via C++
linktitle: Implémenter le système de date 1904
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur. Elle supporte l implémentation du système de date 1904, permettant aux utilisateurs de calculer et de formater selon ce système basé sur le 1er janvier 1904. Cet article explique comment implémenter le système de date 1904 en utilisant la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, système de date 1904, tableur, calcul, formatage
type: docs
weight: 7000
url: /fr/go-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel prend en charge deux systèmes de dates : le système de date 1900 (le système de date par défaut implémenté dans Excel pour Windows) et le système de date 1904. Le système de date 1904 est généralement utilisé pour assurer la compatibilité avec les fichiers Excel Macintosh et est le système par défaut si vous utilisez Excel pour Macintosh. Vous pouvez définir le système de date 1904 pour les fichiers Excel en utilisant Aspose.Cells.

{{% /alert %}}

Pour implémenter le système de date 1904 dans Microsoft Excel (par exemple Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Calcul**.
1. Sélectionnez l'option **Système de date 1904**.
1. Cliquez sur **OK**.

|**Sélection du système de date 1904 dans Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Consultez le code source suivant sur la manière d'accomplir ceci en utilisant les API Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Implement1904DateSystem.go" >}}
