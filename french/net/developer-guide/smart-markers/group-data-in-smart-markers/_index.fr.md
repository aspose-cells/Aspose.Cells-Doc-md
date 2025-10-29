---
title: Comment grouper des données dans Smart Markers
type: docs
weight: 30
url: /fr/net/how-to-group-data-in-smart-markers/
---

## **Scénarios d'utilisation possibles**
Dans certains rapports Excel, vous devrez peut-être fractionner les données en groupes pour les rendre plus faciles à lire et à analyser. L'un des principaux objectifs de la division des données en groupes est d'effectuer des calculs (effectuer des opérations de synthèse) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper des données par champs et de placer des lignes de synthèse entre les ensembles de données ou les groupes de données. Par exemple, si les données sont regroupées par Clients.ClientID, vous pouvez ajouter un enregistrement de synthèse chaque fois que le groupe change.

## **Paramètres de regroupement des données dans Smart Markers**
Voici certains des paramètres de marqueurs intelligents utilisés pour le regroupement de données.
### **group:normal/merge/repeat**
Nous supportons trois types de regroupement entre lesquels vous pouvez choisir.

- **normal** - La valeur du champ de regroupement ne se répète pas pour les enregistrements correspondants dans la colonne; au lieu de cela, elles sont imprimées une fois par groupe de données.
- **fusion** - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le champ de regroupement pour chaque jeu de groupe.
- **répéter** - La valeur du champ de regroupement est répétée pour les enregistrements correspondants.

Par exemple: &=Clients.ClientID(group:merge)
### **skip**
Sauter un nombre spécifié de lignes après chaque groupe.

Par exemple, &=Employés.IDEmployé(group:normal,sauter:1)
### **subtotalN**
Effectue une opération de synthèse pour des données de champ spécifié liées à un champ de regroupement. N représente des nombres entre 1 et 11 qui spécifient la fonction utilisée lors du calcul des sous-totaux dans une liste de données. (1=MOYENNE, 2=NB, 3=NBVAL, 4=MAX, 5=MIN,...9=SUM etc.) Référez-vous à la référence des sous-totaux dans l'aide de Microsoft Excel pour plus de détails.

Le format est en fait stipulé comme suit :
subtotalN:Réf où Réf correspond au champ de regroupement.

Par exemple,

- &=Produits.Unités(subtotal9:Produits.IDProduit) spécifie la fonction de synthèse sur le champ **Unités** par rapport au champ **IDProduit** dans la table **Produits**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) spécifie la fonction de synthèse sur le champ **Col3** groupé par **Col1** dans la table **Tabx**.
- &=Table1.ColonneD(subtotal9:Table1.ColonneA&Table1.ColonneB) spécifie la fonction de synthèse sur le champ **ColonneD** groupé par **ColonneA** et **ColonneB** dans la table **Table1**.

## **Comment grouper des données dans Smart Markers**

Cet exemple illustre certains des paramètres de regroupement en action. Il utilise la base de données Microsoft Access Northwind.mdb et extrait des données de la table nommée "Détails de commande". Nous créons un fichier de conception appelé SmartMarker_Designer.xls dans Microsoft Excel et plaçons des marqueurs intelligents dans différentes cellules des feuilles de calcul. Les marqueurs sont traités pour remplir les feuilles de calcul. Les données sont placées et organisées par un champ de regroupement.

Le fichier de conception comporte deux feuilles de calcul. Dans la première, nous plaçons des marqueurs intelligents avec des paramètres de regroupement comme indiqué dans la capture d'écran ci-dessous. Trois marqueurs intelligents (avec des paramètres de regroupement) sont placés :
&=[Order Details].OrderID(group:merge,skip:1),
&=[Détails de commande].Quantité(soustotal9:Détails de commande.IDCommande), et
&=[Détails de commande].PrixUnitaire(soustotal9:Détails de commande.IDCommande) vont dans A5, B5 et C5 respectivement.

|**La première feuille de travail dans le fichier SmartMarker_Designer.xls, complète avec des marqueurs intelligents**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Dans la deuxième feuille de calcul du fichier de conception, nous plaçons quelques autres marqueurs intelligents comme indiqué dans la figure ci-dessous. Nous plaçons les marqueurs intelligents suivants :
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), et
&=subtotal9:Détails de la commande.CommandeID dans A5, B5, C5, D5 et C6 respectivement.

|**La deuxième feuille de calcul du fichier SmartMarker_Designer.xls, montrant des marqueurs intelligents mixtes.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Voici le code source utilisé dans l'exemple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si vous avez besoin d'ajouter vos propres étiquettes personnalisées aux lignes de résumé ou si vous souhaitez concaténer le nom du champ avec une étiquette, par ex. "Sous-total des commandes", Aspose.Cells vous fournit les attributs Label et LabelPosition, vous pouvez donc placer vos étiquettes personnalisées dans les marqueurs intelligents tout en les concaténant avec les lignes de sous-total dans les données de regroupement. Consultez le document sur Comment Ajouter des Étiquettes Personnalisées à Concaténer avec les Lignes de Sous-total dans les Marqueurs Intelligents pour votre référence.

{{% /alert %}} 
