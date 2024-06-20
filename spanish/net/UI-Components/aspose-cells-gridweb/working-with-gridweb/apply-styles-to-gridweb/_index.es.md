---
title: Aplicar estilos a GridWeb
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, estilo, estilos
description: Este artículo presenta cómo aplicar o establecer un estilo en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tiene su propio aspecto predeterminado, pero es posible cambiar su apariencia. Aspose.Cells.GridWeb proporciona varias propiedades para permitir a los desarrolladores controlar totalmente su apariencia. Este tema discute algunas de esas propiedades.

{{% /alert %}} 
## **Aplicar estilos preestablecidos o personalizados a Aspose.Cells.GridWeb**
### **Estilos preestablecidos**
Para ahorrar esfuerzos a los desarrolladores, Aspose.Cells.GridWeb ofrece algunos estilos preestablecidos. Simplemente selecciona un estilo de la lista para aplicar el estilo.

|**Estilos**|**Esquema de colores**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Cuando se selecciona un estilo en particular, cambia toda la apariencia del control GridWeb. Los desarrolladores pueden seleccionar un Estilo Preestablecido para aplicarse en el Grid durante el diseño, pero esta tarea también se puede llevar a cabo en tiempo de ejecución utilizando la API flexible de Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

El control Aspose.Cells.GridWeb está representado por la clase GridWeb.

{{% /alert %}} 

Para seleccionar un estilo preestablecido:

1. Agregar el control Aspose.Cells.GridWeb a un formulario web.
1. Seleccionar un estilo preestablecido para aplicarlo al control.

El control GridWeb proporciona la propiedad PresetStyle a la que los desarrolladores pueden asignar cualquier estilo preestablecido deseado.

La salida del fragmento de código a continuación se muestra a continuación. 

**Control GridWeb con el estilo Colorful1 aplicado** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Estilo de barra de encabezado**
Si observa el control GridWeb, notará dos barras de encabezado. Uno para las columnas (es decir, A, B, C, D, etc.) y otro para las filas (es decir, 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permite a los desarrolladores controlar la apariencia de estas barras de encabezado. Los desarrolladores pueden establecer el estilo de las barras de encabezado ya sea en tiempo de diseño o en tiempo de ejecución.

{{% alert color="primary" %}} 

El control GridWeb proporciona la propiedad HeaderBarStyle que aplica un estilo en ambas barras de encabezado del control.

{{% /alert %}} 

La salida del ejemplo de código a continuación se muestra aquí. 

**Estilo modificado de la barra de encabezado** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Estilo de la barra de pestañas**
Es posible establecer el estilo de la barra de pestañas. 

**Estilos modificados de las barras de pestañas activas y no activas** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

En la figura anterior, Sheet4 es la pestaña activa, por lo que su apariencia es diferente de las otras pestañas, tal como se define en el ejemplo de código a continuación.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Archivo de estilo personalizado reutilizable**
Aspose.Cells.GridWeb también admite persistir su apariencia o configuraciones de estilo en un archivo. Cuando haya establecido todas las propiedades de apariencia del control GridWeb, puede guardar estas propiedades o configuraciones en un archivo de disco. Este enfoque es muy útil para que los desarrolladores ahorren tiempo y esfuerzos al reutilizar sus antiguas configuraciones de estilo de un archivo de estilo en lugar de establecer todas las propiedades de estilo (o apariencia) del control una por una.
### **Guardando archivo de estilo**
Una vez que haya terminado de establecer las propiedades de estilo, puede guardar la configuración de su estilo en forma de un archivo XML (es porque el archivo de estilo se almacena como un archivo XML) llamando al método SaveCustomStyleFile del control GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

El archivo de estilo guardado está en formato XML, por lo que los desarrolladores también pueden editar este archivo con cualquier editor de texto, si así lo desean.

{{% /alert %}} 
### **Cargando archivo de estilo**
Para aplicar la configuración de estilo de un archivo de estilo existente al control GridWeb, los desarrolladores pueden establecer la ruta del archivo de estilo en la propiedad CustomStyleFileName del control. Pero, antes de hacer eso, es necesario establecer la propiedad PresetStyle del control en Personalizado. Esto se debe a que el archivo de estilo contiene información de estilo personalizado que ya está definida por un desarrollador.

{{% alert color="primary" %}} 

También es posible cargar o guardar un archivo de estilo utilizando Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Cargar un archivo de estilo en el control GridWeb no afecta la configuración de formato de las celdas del control.

{{% /alert %}} 
### **Formato estándar de la plantilla de estilo XML**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
