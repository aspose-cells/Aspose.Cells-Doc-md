---
title: Lecture et écriture de table de requêtes de feuille de calcul
type: docs
weight: 40
url: /fr/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET fournit la collection Worksheet.QueryTables qui retourne l’objet de type QueryTable par index. Elle possède les deux propriétés suivantes

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Ce sont deux valeurs booléennes. Vous pouvez les afficher dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}}

## Lecture et écriture de table de requêtes de feuille de calcul

Le code d'exemple suivant lit la première QueryTable de la première feuille de calcul, puis imprime les deux propriétés de QueryTable. Ensuite, il définit QueryTable.PreserveFormatting sur true.

Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5115533.xlsx)
- [Fichier Excel de Sortie](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Sortie de la Console

Voici la sortie de la console du code d'exemple ci-dessus

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Récupérer la plage de résultats de la table de requête

Aspose.Cells pour Python via .NET offre l’option de lire l’adresse, c’est-à-dire la plage de résultats des cellules pour une table de requête. Le code suivant démontre cette fonctionnalité en lisant l’adresse de la plage de résultats pour une table de requête. Le fichier d’échantillon peut être téléchargé [ici](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

