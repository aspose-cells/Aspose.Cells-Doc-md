---
title: Editor de Hoja de Cálculo  Componentes
type: docs
weight: 50
url: /es/java/spreadsheet-editor-components/
---

**Tabla de contenidos**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Vista de hoja de cálculo](#SpreadsheetEditor-Components-WorksheetView)
- [Servicio de libro de trabajo](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

El Editor de Hoja de Cálculo HTML5 está construido a partir de varios componentes que se unen para formar el sistema completo. Aquí describimos el propósito y el papel de cada uno.
### **Index.html**
Es una página JSF que describe la interfaz de usuario del editor y el punto de conexión principal de nuestra aplicación. Toda la interacción que se realiza entre el navegador web y el servidor se realiza a través de este punto de conexión.

Además de definir la interfaz de usuario, todos los servicios de back-end se adjuntan aquí utilizando tecnologías JSF. Cuando el usuario interactúa con los eventos de la interfaz de usuario, los datos se pasan de un lado a otro entre los servicios y el usuario para completar nuestras tareas, por ejemplo, la exportación de hojas de cálculo.

Tiene dos áreas principales de interés.

**Cinta**

El área de barra de herramientas con pestañas en la parte superior se llama cinta, técnicamente. Contiene botones, menús desplegables, botones de radio, menús de texto y algunos campos ocultos que se utilizan para realizar muchas operaciones en la hoja de cálculo. Estos botones, cuando se hace clic, envían comandos al servidor y actualizan la hoja en consecuencia.

**Hoja**

La hoja son las filas y columnas. Cuando se hace clic en las celdas, la cinta se actualiza en consecuencia sin enviar solicitudes al servidor, ya que todos los datos que necesita la cinta están adjuntos a cada celda. La cinta también realiza un seguimiento de la celda, fila y columna seleccionadas cuando el usuario navega por la hoja.

Cada celda tiene su propio editor en línea que se hace visible cuando una celda está en modo de edición.
### **Vista de hoja de cálculo**
Es un bean de back-end JSF de alcance de vista responsable de administrar el contenido dinámico de la interfaz de usuario descrito en index.html. Tiene controladores de eventos para las solicitudes Ajax que se activan a medida que el usuario interactúa con la interfaz de usuario.
### **Servicio de libro de trabajo**
El WorkbookService es un bean de back-end JSF de alcance de vista. Funciona como un componente de servicio y carga y descarga la hoja de cálculo con la ayuda de otros servicios. Tiene los siguientes puntos finales:

**init**

El **init** es un método **PostConstruct** que se ejecuta justo después de que la creación del objeto se completa por el Servidor de Aplicaciones Java. Verifica el parámetro **url** en el mapa de parámetros de la solicitud y carga la hoja de cálculo correspondiente desde la ubicación dada, si es posible.

**destroy**

Es responsable de limpiar todos los recursos adquiridos cuando ya no son necesarios.
### **LoaderService**
Crea instancias de la hoja de cálculo y las mantiene en memoria mientras son necesarias.
### **CellsService**
El **CellsService** gestiona la caché de filas, columnas, celdas, formato y estructura de las hojas de cálculo.
