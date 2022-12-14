---
title: Usando Aspose.Cells.GridDesktop en la aplicación WPF
type: docs
weight: 50
url: /es/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 En este artículo, se muestra cómo usar el Diseñador de Windows Presentation Foundation (WPF) para Visual Studio para hospedar un control de Formularios Windows como Aspose.Cells.GridDesktop en una aplicación WPF.
Usaremos Visual Studio 2015 para demostrar el proceso; sin embargo, puede usar cualquier versión, incluida Visual Studio 2008 o posterior.

{{% /alert %}} 

Este tutorial lo guiará a través del proceso de agregar el control Aspose.Cells.GridDesktop a una aplicación WPF. Necesita cualquier versión del IDE de Visual Studio que admita el desarrollo de WPF para probar esto de su parte.
## **Cree una aplicación WPF usando Visual Studio**
 Primero cree una aplicación WPF usando Visual Studio IDE. Haga clic en**Expediente** >> **Nuevo** >> **Proyecto** menú y seleccione**Aplicación WPF** de Plantillas, asigne un nombre al proyecto y haga clic en**OK**. Puede orientar su proyecto a cualquier Framework .NET superior a 2.0, sin embargo, no puede usar el perfil de cliente .NET Frameworks.
## **Agregar referencias a los espacios de nombres requeridos**
Agregue las referencias a los siguientes ensamblajes haciendo clic con el botón derecho en la ventana Referencias desde el Explorador de soluciones y seleccione el menú Agregar referencia.

- Ensamblado de WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Windows Ensamblaje de formularios (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop ensamblado (Aspose.Cells.GridDesktop.dll).

Esta acción agrega los ensamblajes necesarios a la aplicación, es decir; copia los ensamblajes en la carpeta Bin de la aplicación.
## **Agregar referencias a XAML**
A continuación, vaya al archivo XAML y agregue los siguientes espacios de nombres y referencias de ensamblado dentro de la etiqueta Windows.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**La etiqueta final Windows tendrá un aspecto similar al que se muestra a continuación.**

![todo:imagen_alternativa_texto](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Agregue el control Aspose.Cells.GridDesktop a XAML**
 Simplemente agregue el siguiente código dentro de la etiqueta Grid en XAML. los**WindowsFormsHost** se utiliza para alojar el control de formularios Windows y**gridEscritorio:GridEscritorio** La etiqueta representa el control Aspose.Cells.GridDesktop. También puede nombrar el control para que se pueda hacer referencia a él fácilmente en el código.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**El XAML final tendrá el siguiente aspecto.** 

![todo:imagen_alternativa_texto](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Utilice Aspose.Cells.GridDesktop**
Ahora podemos acceder y usar el control Aspose.Cells.GridDesktop en el archivo .cs como cualquier otra aplicación de formularios Windows. Para mantener la demostración simple, solo cargamos una hoja de cálculo de muestra en el control Aspose.Cells.GridDesktop y la guardamos nuevamente. Además, hemos utilizado el evento FrameworkElement_OnLoaded para activar las siguientes declaraciones.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Construir y ejecutar**
 Ahora, compila y ejecuta la aplicación usando**F5** o**comienzo** en la interfaz de usuario de Visual Studio.
