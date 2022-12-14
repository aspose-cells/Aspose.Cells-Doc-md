---
title: Personnalisation des graphiques
type: docs
weight: 40
url: /fr/net/customizing-charts/
---
{{% alert color="primary" %}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné les graphiques standard qui ont leurs paramètres de mise en forme standard. Nous définissons uniquement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells prennent également en charge la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de format.

Les développeurs peuvent créer des graphiques personnalisés au moment de l'exécution à l'aide de Aspose.Cells.

 Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un[**Série**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) objet alors que[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) l'objet sert de collection de[**Série**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)objets. Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans le[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objet).

L'exemple de code ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un histogramme pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique à colonnes, combiné à un graphique linéaire, à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Actuellement, Aspose.Cells ne prend en charge que les graphiques personnalisés qui combinent des graphiques à secteurs, linéaires, à colonnes et à colonnes, mais davantage de graphiques seront pris en charge dans les versions futures.

{{% /alert %}}
