---
title: Comment utiliser le paramètre de plage dans SmartMarkers
type: docs
weight: 10
url: /fr/net/how-to-use-range-parameter-in-smart-markers/
---

## **Pourquoi utiliser le paramètre de plage dans Smart Markers**
Le paramètre de plage dans SmartMarkers est utilisé pour contrôler précisément où et comment les données sont placées dans un modèle Excel lors de sa remplissage avec des données provenant d'une source (par exemple, JSON, bases de données). Cela permet de gérer la sortie de données dynamique, notamment lorsqu'il s'agit de tableaux de longueur variable ou de regroupements complexes.

1. Contrôler le placement des données et éviter le chevauchement : Lorsque les sources de données contiennent des tableaux dynamiques (par exemple, nombre variable d'éléments par enregistrement), le paramètre de plage garantit que les données sont remplies dans une plage Excel définie, évitant ainsi le débordement dans les cellules ou sections adjacentes.

2. Gérer les formules de tableau dynamiques : Pour des opérations telles que la transposition de tableaux dynamiques (par exemple, &=TRANSPOSE(DataArray)), le paramètre de plage garantit que le résultat s'adapte à la taille réelle des données sans laisser de valeurs résiduelles (par exemple, zéros dans les champs vides) provenant d'opérations précédentes.

3. Supporter le regroupement et les données hiérarchiques : Lorsque les données nécessitent un regroupement (par exemple, structures JSON imbriquées), le paramètre de plage aide à définir des zones de sortie hiérarchiques. Par exemple, regrouper des enregistrements sous une catégorie parent sans ajustement manuel des lignes. Sans plage définie, SmartMarkers pourrait ne pas représenter avec précision les relations imbriquées, surtout si les sources de données ne comportent pas de hiérarchies explicites.

4. Améliorer la conception et la cohérence du modèle : En spécifiant des plages, les utilisateurs garantissent que la mise en forme, les formules et les bordures sont appliquées de manière cohérente sur la zone de sortie. Cela évite des problèmes comme un style de cellule incohérent ou des formules cassées dans les rapports générés.

5. Optimiser les performances et le tri des données : Le paramètre de plage permet aux outils de trier préalablement les sources de données avant de remplir les modèles, assurant que les données regroupées apparaissent dans le bon ordre.

## **Comment utiliser le paramètre de plage dans SmartMarkers**
Parfois, vous devez trier et effectuer d'autres opérations sur une plage dans SmartMarkers. Aspose.Cells permet d'utiliser le paramètre de plage dans SmartMarkers. Veuillez consulter le [fichier de modèle](range.xlsx), le [fichier JSON](range.json) et la capture d'écran du fichier Excel généré avec le code suivant.

|**La première feuille du fichier range.xlsx montrant les smart markers.**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**La capture d'écran du fichier Excel de sortie.**|
| :- |
|![todo:image_alt_text](range_result.png)|

Données JSON comme suit :
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
L'exemple suivant montre comment cela fonctionne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
