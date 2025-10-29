---
title: Importation intelligente d objets imbriqués dans Excel avec des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/how-to-import-nested-objects-with-smart-markers/
---

## **Pourquoi utiliser des objets imbriqués pour les marqueurs intelligents**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Représentation hiérarchique des données : Les données du monde réel sont intrinsèquement imbriquées (par exemple, une commande contient un client, qui possède une adresse). Les objets imbriqués reflètent cette structure, évitant les champs aplatis/artificiels tels que client_ville.
2. Éviter les collisions de noms : Les structures plates risquent des conflits (par exemple, nom_produit vs nom_fournisseur). L'imbrication limite naturellement l'espace de noms :
<<product.name>> vs. <<supplier.name>>.
3. Modularité & Réutilisabilité : Réutiliser les sous-objets dans différents contextes, l'objet Adresse peut être intégré dans Marqueur Client, Fournisseur ou Employé. Les modifications apportées à Adresse se propagent universellement.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Support des frameworks/outils : Les moteurs modernes (par exemple, Handlebars, React, FoxPro) résolvent nativement les chemins imbriqués. Aligné avec JSON/APIs où les données imbriquées sont la norme.

## **Comment importer des types anonymes ou des objets personnalisés avec des marqueurs intelligents**
Aspose.Cells prend également en charge les types anonymes ou les objets personnalisés dans les marqueurs intelligents. L'exemple suivant montre comment cela fonctionne. Pour importer des données à partir d'objets dynamiques à l'aide de Smart Markers, consultez l'article suivant :

[Importation à partir d'un objet dynamique en tant que source de données](/cells/fr/net/importer-des-donnees-dans-la-feuille-de-calcul/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Comment importer des objets imbriqués avec des marqueurs intelligents**
Aspose.Cells prend en charge les objets imbriqués dans les marqueurs intelligents, les objets imbriqués doivent être simples. Nous utilisons un fichier de modèle simple. Consultez la feuille de calcul de conception qui contient quelques marqueurs intelligents imbriqués.

|**La première feuille de calcul du fichier SM_NestedObjects.xlsx montrant des marqueurs intelligents imbriqués.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'exemple suivant montre comment cela fonctionne.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Comment importer une liste générique en tant qu'objet imbriqué avec des marqueurs intelligents**
Aspose.Cells prend désormais en charge l'utilisation d'une liste générique comme objet imbriqué. Veuillez vérifier la capture d'écran du fichier Excel généré avec le code suivant. Comme vous pouvez le voir dans la capture d'écran, un objet Teacher contient plusieurs objets Student imbriqués.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Comment importer des objets imbriqués pas ligne par ligne avec des marqueurs intelligents**
La méthode de traitement par défaut actuelle consiste à traiter les marqueurs intelligents ligne par ligne. Mais parfois, les marqueurs intelligents de la même table de données doivent être traités ensemble, peu importe s'ils se trouvent dans la même ligne ou non, alors vous devez spécifier une plage nommée "_CellulesMarqueursIntelligents" et spécifier WorkbookDesigner.LineByLine comme faux avant d'appeler le traitement. 
s'ils sont dans la même ligne ou non, alors vous devez spécifier une plage nommée "_CellsSmartMarkers" et spécifier WorkbookDesigner.LineByLine comme faux avant d'appeler le traitement.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
