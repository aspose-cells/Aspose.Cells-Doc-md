---
title: Uso de Aspose.Cells.GridDesktop en aplicación WPF
type: docs
weight: 50
url: /es/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Este artículo introduce cómo usar GridDesktop en una aplicación WPF.
---

{{% alert color="primary" %}} 

Este artículo demuestra cómo usar el Diseñador de Windows Presentation Foundation (WPF) para Visual Studio para alojar un control de Windows Forms como Aspose.Cells.GridDesktop en una aplicación WPF. 
Utilizaremos Visual Studio 2015 para demostrar el proceso, sin embargo, puedes utilizar cualquier versión, incluida Visual Studio 2008 o posterior.

{{% /alert %}} 

Este tutorial te guiará a través del proceso de agregar el control Aspose.Cells.GridDesktop a una aplicación WPF. Necesitas cualquier versión del entorno de desarrollo Visual Studio que admita el desarrollo de aplicaciones WPF para probar esto en tu equipo.
## **Crea una aplicación WPF usando Visual Studio**
Primero crea una aplicación WPF utilizando el entorno de desarrollo Visual Studio. Haz clic en **Archivo** >> **Nuevo** >> **Proyecto** y selecciona **Aplicación WPF** en Plantillas, nombra el proyecto y haz clic en **Aceptar**. Puedes apuntar tu proyecto a cualquier versión de .NET Framework superior a 2.0, sin embargo, no puedes usar perfiles de cliente de .NET Framework.
## **Agregar referencias a los espacios de nombres requeridos**
Agregue las referencias a las siguientes librerías haciendo clic derecho en Referencias desde la ventana Explorador de soluciones y selecciona el menú Agregar referencia.

- Librería WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Librería Windows Forms (System.Windows.Forms.dll).
- Librería Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

Esta acción agrega las librerías requeridas a la aplicación, es decir; copia las librerías a la carpeta Bin de la aplicación.
## **Agregar referencias a XAML**
A continuación, vaya al archivo XAML y agregue los siguientes espacios de nombres y referencias de librerías dentro de la etiqueta Windows.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**La etiqueta Windows final se verá similar a como se muestra a continuación.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Agregar control Aspose.Cells.GridDesktop a XAML**
Simplemente agregue el siguiente código dentro de la etiqueta Grid en XAML. La etiqueta **WindowsFormsHost** se utiliza para alojar el control Windows Forms y la etiqueta **gridDesktop:GridDesktop** representa el control Aspose.Cells.GridDesktop. También puede nombrar el control para que se pueda hacer referencia fácilmente en el código.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**El XAML final se verá como se muestra a continuación.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Usar Aspose.Cells.GridDesktop**
Ahora podemos acceder y usar el control Aspose.Cells.GridDesktop en el archivo .cs al igual que cualquier otra aplicación de Windows Forms. Con el fin de mantener la demostración simple, simplemente estamos cargando una hoja de cálculo de muestra en el control Aspose.Cells.GridDesktop y guardándola de nuevo. Además, hemos utilizado el evento FrameworkElement_OnLoaded para activar las siguientes instrucciones.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Compilar y ejecutar**
Ahora, compile y ejecute la aplicación usando **F5** o el botón **Iniciar** en la interfaz de usuario de Visual Studio.
