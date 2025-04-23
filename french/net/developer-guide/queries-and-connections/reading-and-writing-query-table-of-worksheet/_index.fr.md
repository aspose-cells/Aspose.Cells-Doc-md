---
title: Lecture et écriture de table de requêtes de feuille de calcul
type: docs
weight: 40
url: /fr/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells fournit une collection Worksheet.QueryTables qui renvoie l'objet de type QueryTable par index. Il dispose des deux propriétés suivantes

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ce sont deux valeurs booléennes. Vous pouvez les afficher dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}}

## Lecture et écriture de table de requêtes de feuille de calcul

Le code d'exemple suivant lit la première QueryTable de la première feuille de calcul, puis imprime les deux propriétés de QueryTable. Ensuite, il définit QueryTable.PreserveFormatting sur true.

Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5115533.xlsx)
- [Fichier Excel de Sortie](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Sortie de la Console

Voici la sortie de la console du code d'exemple ci-dessus

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Récupérer la plage de résultats de la table de requête

Aspose.Cells offre la possibilité de lire l'adresse, c'est-à-dire la plage de résultats des cellules pour une table de requête. Le code suivant démontre cette fonctionnalité en lisant l'adresse de la plage de résultats pour une table de requête. Le fichier d'exemple peut être téléchargé [ici](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
