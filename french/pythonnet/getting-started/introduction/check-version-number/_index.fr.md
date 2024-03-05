---
title: Vérifier le numéro de version
type: docs
weight: 80
url: /fr/python-net/check-version-number/
---
{{% alert color="primary" %}}

Vous vous demandez quelle version de Aspose.Cells vous utilisez ? Nous publions régulièrement de nouvelles versions de Aspose.Cells, à la fois pour introduire de nouvelles fonctionnalités et pour résoudre des problèmes. Le numéro de version comprend le numéro de version majeure, le numéro de version mineure et le numéro de version du correctif. Chaque nombre doit être un nombre entier à partir de 0. Le format est le suivant :

correctif majeur.mineur

Lorsque nous publions une nouvelle version de Aspose.Cells, nous mettons à jour le numéro de version.

Cet article explique comment vérifier manuellement quelle version de Aspose.Cells est installée sur le système et en utilisant le Aspose.Cells API.

{{% /alert %}}

## **Vérifier manuellement le numéro de version**

Pour savoir quelle version de Aspose.Cells vous utilisez manuellement :

1.  Cliquez avec le bouton droit sur le fichier Aspose.Cells.dll et sélectionnez**Propriétés**.
1. Cliquez sur l'onglet Version (ou Détails) pour vérifier le numéro de version.

## **Vérifiez le numéro de version à l'aide du Aspose.Cells API**

Pour savoir quelle version de Aspose.Cells vous utilisez via API, utilisez la méthode statique GetVersion de la classe CellsHelper pour obtenir le numéro de version de Aspose.Cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
