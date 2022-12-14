---
title: Appliquer des styles à GridWeb
type: docs
weight: 20
url: /fr/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb a sa propre apparence par défaut mais il est possible de changer son apparence. Aspose.Cells.GridWeb fournit plusieurs propriétés pour permettre aux développeurs de contrôler entièrement son apparence. Cette rubrique décrit certaines de ces propriétés.

{{% /alert %}} 
## **Application de styles prédéfinis ou personnalisés à Aspose.Cells.GridWeb**
### **Styles prédéfinis**
Pour économiser les efforts des développeurs, Aspose.Cells.GridWeb propose des styles prédéfinis. Sélectionnez simplement un style dans la liste pour appliquer le style.

|**modes**|**Schéma de couleur**|
|:- |:- |
|Standard|Argent|
|Coloré1|Rose|
|Coloré2|Bleu|
|Professionnel1|cyan|
|Professionnel2|Cyan à nouveau|
|Traditionnel1|Sombre|
|Traditionnel2|Gris|
|Personnalisé|Personnalisé|
Lorsqu'un style particulier est sélectionné, il modifie toute l'apparence du contrôle GridWeb. Les développeurs peuvent sélectionner un style prédéfini à appliquer sur la grille au moment de la conception, mais cette tâche peut également être accomplie lors de l'exécution à l'aide du flexible API de Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells.Le contrôle GridWeb est représenté par la classe GridWeb.

{{% /alert %}} 

Pour sélectionner un style prédéfini :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Sélectionnez un style prédéfini à appliquer sur le contrôle.

Le contrôle GridWeb fournit la propriété PresetStyle à laquelle les développeurs peuvent affecter n'importe quel style prédéfini souhaité.

 La sortie de l'extrait de code ci-dessous est illustrée ci-dessous.

**Contrôle GridWeb avec le style Colorful1 appliqué dessus** 

![tâche : image_autre_texte](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Style de la barre d'en-tête**
Si vous regardez le contrôle GridWeb, vous remarquerez deux barres d'en-tête. Un pour les colonnes (c'est-à-dire A, B, C, D, etc.) et l'autre pour les lignes (c'est-à-dire 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permet aux développeurs de contrôler l'apparence de ces barres d'en-tête. Les développeurs peuvent définir le style des barres d'en-tête au moment de la conception ou de l'exécution.

{{% alert color="primary" %}} 

Le contrôle GridWeb fournit la propriété HeaderBarStyle qui applique un style sur les deux barres d'en-tête du contrôle.

{{% /alert %}} 

 La sortie de l'exemple de code ci-dessous est illustrée ici.

**Style modifié de la barre d'en-tête** 

![tâche : image_autre_texte](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Style de la barre d'onglets**
 Il est possible de définir le style de la barre d'onglets.

**Styles modifiés des barres d'onglets actives et non actives** 

![tâche : image_autre_texte](apply-styles-to-gridweb_3.png)

Dans la figure ci-dessus, Sheet4 est l'onglet actif, son apparence est donc différente des autres onglets, comme défini par l'exemple de code ci-dessous.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Fichier de style personnalisé réutilisable**
Aspose.Cells.GridWeb prend également en charge la persistance de ses paramètres d'apparence ou de style dans un fichier. Lorsque vous avez défini toutes les propriétés d'apparence du contrôle GridWeb, vous pouvez enregistrer ces propriétés ou paramètres dans un fichier disque. Cette approche est très utile pour les développeurs qui économisent leur temps et leurs efforts en réutilisant leurs anciennes configurations de style à partir d'un fichier de style au lieu de définir toutes les propriétés de style (ou d'apparence) du contrôle une par une.
### **Enregistrement du fichier de style**
Une fois que vous avez terminé de définir les propriétés de style, vous pouvez enregistrer vos paramètres de configuration de style sous la forme d'un fichier XML (c'est parce que ce fichier Style est stocké sous forme de fichier XML) en appelant la méthode SaveCustomStyleFile du contrôle GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Le fichier de style enregistré est au format XML. Ainsi, les développeurs peuvent également modifier ce fichier avec n'importe quel éditeur de texte, s'ils le souhaitent.

{{% /alert %}} 
### **Chargement du fichier de style**
Pour appliquer les paramètres de style d'un fichier de style existant au contrôle GridWeb, les développeurs peuvent définir le chemin du fichier de style sur la propriété CustomStyleFileName du contrôle. Mais, avant de faire cela, il est nécessaire de définir la propriété PresetStyle du contrôle sur Custom. C'est parce que ce fichier de style contient des informations de style personnalisées qui sont déjà définies par un développeur.

{{% alert color="primary" %}} 

Il est également possible de charger ou d'enregistrer un fichier de style à l'aide de Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Le chargement du fichier de style dans le contrôle GridWeb n'affecte pas les paramètres de mise en forme des cellules du contrôle.

{{% /alert %}} 
### **Format standard du modèle de style XML**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
