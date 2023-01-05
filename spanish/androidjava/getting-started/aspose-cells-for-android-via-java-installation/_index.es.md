---
title: Aspose.Cells for Android via Java Instalación
type: docs
weight: 30
url: /es/java/aspose-cells-for-android-via-java-installation/
---
## **Requisitos del sistema**
Aspose.Cells for Android via Java es independiente de la plataforma y se puede usar en cualquier plataforma donde esté instalado el entorno de Android Runtime y se ejecutará en sistemas Android con Android OS 2.0 o superior. Actualmente, el componente ha sido probado con:

- Android 5.1 versión 22
## **Instale Aspose.Cells for Android via Java desde el repositorio Maven**
1. Agregue el repositorio maven a su build.gradle
1. Agregar 'Aspose.Cells for Android via Java' JAR como dependencia

{{< highlight "java" >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Cómo usar Aspose.Cells for Android via Java**
Este tema lo guiará a través de los pasos necesarios para configurar Aspose.Cells for Android via Java en el IDE de Android Studio, asumiendo que ya tiene la última versión de Android Studio instalada en su máquina y que también adquirió la última versión del paquete Aspose.Cells for Android via Java.

{{% alert color="primary" %}} 

Si aún no ha instalado Android Studio, primero debe adquirir la configuración de Android Studio e instalarla en su máquina. Puede descargar la última versión de Android Studio desde[aquí](https://developer.android.com/studio/index.html#win-bundle) mientras que los detalles sobre cómo instalar el IDE están disponibles[aquí](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 El paquete Aspose.Cells for Android via Java se puede descargar desde[aquí](https://downloads.aspose.com/cells/androidjava). Tenga en cuenta que cada paquete de lanzamiento de Aspose.Cells for Android via Java consta principalmente de 2 archivos, como se detalla a continuación.

- **aspose-cells-xxxjar** es el archivo de la biblioteca principal que contiene todos los espacios de nombres de Aspose.Cells for Android via Java API.
- **aspose-cells-xxx-libs.apk** es el APK que contiene el bcprov-jdk15-146.jar de terceros utilizado para las funciones de cifrado y descifrado ofrecidas por Aspose.Cells for Android via Java API.

{{% /alert %}} 
### **Primeros pasos con Aspose.Cells for Android via Java en Android Studio**
Una vez que se carga el IDE de Android Studio, haga clic en Archivo > Nuevo > Nuevo proyecto como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_1.png)

También puede crear un nuevo proyecto desde la pantalla de bienvenida de Android Studio, como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_2.png)

A continuación, se le pedirá que especifique el nombre de la aplicación, el dominio y la ubicación para almacenar los archivos del proyecto. Puede optar por cambiar los valores predeterminados según su elección o dejarlos como están y hacer clic en Siguiente.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_3.png)

En el siguiente paso, debe especificar el dispositivo Android que desea alojar/ejecutar su aplicación. Una vez seleccionado, haga clic en el botón Siguiente.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_4.png)

Ahora debe seleccionar la actividad de una lista predefinida de plantillas. Para simplificar la demostración, hemos seleccionado la plantilla Actividad vacía como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_5.png)

Haga clic en el botón Finalizar en el cuadro de diálogo Personalizar la actividad, ya que mantendremos todas las configuraciones predeterminadas tal como están.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_6.png)

Tan pronto como haga clic en el botón Finalizar en el paso anterior, el IDE comenzará a construir el proyecto como se muestra a continuación. Deje que termine o haga clic en el botón Cancelar.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_7.png)

Ahora que el proyecto se ha cargado en el IDE, sin embargo, es posible que desee cambiar la vista a Proyecto para que pueda ver la jerarquía completa de los archivos del proyecto. Para cambiar la vista, consulte la siguiente instantánea.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_8.png)

 Después de cambiar la vista a Proyecto, busque y cargue el**construir.gradle** archivo en el editor y pegue el siguiente fragmento como se muestra a continuación.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_9.png)

A continuación, agregaremos el Jar Aspose.Cells for Android via Java al proyecto. Hay 2 pasos importantes como se detalla a continuación.

-  Copie manualmente el tarro Aspose.Cells for Android via Java en el**\aplicación\libs** carpeta.
- Agregue Aspose.Cells for Android via Java Jar como biblioteca al módulo como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_10.png)

Se le pedirá que seleccione el módulo al que desea agregar el Aspose.Cells for Java.Android Jar como biblioteca. Elija adecuadamente y haga clic en Aceptar.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_11.png)

 También debe agregar el archivo APK al proyecto. Tienes que copiar el APK al**\app\src\main\activos**carpeta. Si no tiene la carpeta de activos en la carpeta principal, puede crear una haciendo clic con el botón derecho en el nodo principal en la vista Proyecto. Seleccione Nuevo > Carpeta > Carpeta de activos.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_12.png)

Una vez que se ha agregado el APK al proyecto, el proyecto debe cargarlo. Hay 2 formas de cargar el APK de la siguiente manera.

- Cargue el APK en una clase de aplicación personalizada con el fragmento que se proporciona a continuación y registre la clase de aplicación personalizada en AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Cargue el APK en el método OnCreate de MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Ahora estamos listos para escribir el código. Para que la demostración sea fácil de entender, hemos agregado un widget de botón al diseño y manejaremos su evento de clic de la siguiente manera.

{{< highlight "java" >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

Cuando ejecuta la aplicación usando el botón de reproducción en la interfaz IDE (o usando SHIFT + F10), el emulador cargará la aplicación como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_13.png)

Al hacer clic en el botón del emulador, se ejecutará el código para crear una nueva hoja de cálculo en la carpeta de almacenamiento externo del emulador. Puede acceder al archivo desde Android Device Monitor como se muestra a continuación.

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_14.png)

![todo:imagen_alternativa_texto](aspose-cells-for-android-via-java-installation_15.png)


