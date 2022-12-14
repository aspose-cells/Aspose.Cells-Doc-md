---
title: Table de requête de lecture et d'écriture de la feuille de calcul
type: docs
weight: 40
url: /fr/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells fournit la collection Worksheet.QueryTables qui renvoie l'objet de type QueryTable par index. Il a les deux propriétés suivantes

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ce sont deux valeurs booléennes. Vous pouvez les visualiser dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}}

## Table de requête de lecture et d'écriture de la feuille de calcul

L'exemple de code suivant lit le premier QueryTable de la première feuille de calcul, puis imprime les deux propriétés QueryTable. Ensuite, il définit QueryTable.PreserveFormatting sur true.

Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel source](5115533.xlsx)
- [Fichier Excel de sortie](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Sortie console

Voici la sortie console de l'exemple de code ci-dessus

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Récupérer la plage de résultats de la table de requête

 Aspose.Cells fournit l'option de lire l'adresse, c'est-à-dire la plage de résultats de cellules pour une table de requête. Le code suivant illustre cette fonctionnalité en lisant l'adresse de la plage de résultats pour une table de requête. Un exemple de fichier peut être téléchargé[ici](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
