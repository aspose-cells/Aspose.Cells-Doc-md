---
title: Vérifiez le numéro de version
type: docs
weight: 80
url: /fr/net/check-version-number/
---

{{% alert color="primary" %}}

Vous vous demandez quelle version d'Aspose.Cells vous utilisez? Nous publions régulièrement de nouvelles versions d'Aspose.Cells, à la fois pour introduire de nouvelles fonctionnalités et pour corriger des problèmes. Le numéro de version se compose du numéro de version majeure, du numéro de version mineure et du numéro de correction. Chaque nombre doit être un entier de 0 à plus. Le format est le suivant:

majeur.mineur.correction

Lorsque nous publions une nouvelle version d'Aspose.Cells, nous mettons à jour le numéro de version.

Cet article explique comment vérifier manuellement quelle version d'Aspose.Cells est installée sur le système et en utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Vérifier le numéro de version manuellement**

Pour savoir quelle version d'Aspose.Cells vous utilisez manuellement:

1. Cliquez avec le bouton droit sur le fichier Aspose.Cells.dll et sélectionnez **Propriétés**.
1. Cliquez sur l'onglet Version (ou Détails) pour vérifier le numéro de version.

## **Vérifier le numéro de version en utilisant l'API Aspose.Cells**

Pour savoir quelle version d'Aspose.Cells vous utilisez via l'API, utilisez la méthode statique GetVersion de la classe [CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) pour obtenir le numéro de version d'Aspose.Cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
