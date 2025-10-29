---
title: Ajouter une connexion Pivot avec Golang via C++
linktitle: Ajouter une connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/go-cpp/add-pivot-connection/
description: Apprenez comment ajouter une connexion pivot avec la bibliothèque Aspose.Cells en utilisant C++.
keywords: Ajouter une connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez associer un segment de rapport et un tableau croisé dynamique dans Excel, vous devez cliquer avec le bouton droit sur le segment de rapport et sélectionner l'élément "Connexions de rapport...". Dans la liste des options, vous pouvez agir sur la case à cocher. De même, si vous souhaitez associer un segment de rapport et un tableau croisé dynamique à l'aide de l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/). Cela associera le segment de rapport et le tableau croisé dynamique.

## **Associer une trancheuse et un tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](add-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède à la trancheuse et associe ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous forme de [fichier Excel de sortie](add-pivot-connection-out.xlsx). 

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
