---
title: hur man bygger en samarbetsmöjlighet i Excel med GridJs
type: docs
weight: 260
url: /sv/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs, samarbetsvillig, excel redigerare, kalkylblad, java
description: Denna artikel introducerar hur man bygger en samarbetsredigerare i Excel med Aspose.Cells.GridJs för Java.
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# Guide för samarbetsredigerare i Excel

## Arkitekturöversikt

Följande diagram visar hur GridJs möjliggör samarbetsredigering med flera användare, 
en Spring Boot-backend, WebSocket-kommunikation och en MySQL-databas för tillståndshantering.

![GridJs Collaborativ Arkitektur](gridjs_collaborative_architecture.png)

## Förutsättningar

Innan du börjar, se till att du har installerat följande:

- **Java 8+**  
- **Maven**  
- **MySQL** (eller en annan stödd SQL-databas)  
- (Valfritt) **Docker** om du föredrar att köra i containrar  
- En giltig **Aspose.Cells-licens** (eller [tillfällig licens](https://purchase.aspose.com/temporary-license))  

---

## Step 1: Clone the Demo Project

Clone the official [Aspose.Cells GridJs demo repository](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs.Collaborative):

```bash
git clone https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java.git
cd Aspose.Cells-for-Java/Examples.GridJs.Collaborative
```

---

## Step 2: Configure Collaborative Mode

Open the [`src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties) file and adjust the settings:

```properties
# Directory containing spreadsheet files
testconfig.ListDir=/app/wb

# Directory for storing cache files
testconfig.CachePath=/app/grid_cache

# Aspose.Cells license file
testconfig.AsposeLicensePath=/app/license

# Enable collaborative mode
gridjs.iscollabrative=true

# Database connection (example: MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/gridjsdemodb?createDatabaseIfNotExist=true&useUnicode=true&serverTimezone=UTC&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.sql.init.platform=mysql
```

Detta gör att flera användare kan redigera samma kalkylblad samtidigt.  
Ändringar lagras i databasen och synkroniseras mellan klienterna i realtid.

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

Eller direkt från huvudklassen:

```
src/main/java/com/aspose/gridjsdemo/usermanagement/UserManagementApplication.java
```

---

## Step 4: Test Collaborative Editing

Open your browser and navigate to:  
👉 `http://localhost:8080/gridjsdemo/list`

Steps:

1. A login page appears. Click **Create User** to register User1 and log in. You will then see the file list.  
2. Open a file from the list. The spreadsheet editor will load.  
3. Copy the same URL into another browser window. It will redirect to the login page. Create User2 and log in.  
4. Both users now see the same spreadsheet.  
5. If User1 edits the spreadsheet, User2 will see the changes in real time.  
6. If User2 edits, User1 will see the changes as well.  
7. Users can also download and save the file.  

---

## Steg 5: Kör i Docker (Valfritt)

Om du kör i Docker, redigera rad 10 i [`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml) för att mappa licensfilen.  

Till exempel, om din licensfil är på `C:/license/aspose.lic`:

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

Det här mappar den lokala filen till containern.

Sedan bygger och kör du:

```bash
docker-compose up --build
```

Åtkomst till appen på:  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

I server-side konfiguration [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

Eller globalt:

```java
Config.setCollaborative(true);
```

I klient-side laddningsalternativ [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html):

```js
const option = {
    //..... other options
    //here we shall set true for collaborative mode
    isCollaborative: true
    //..... other options
};
```

---

### 2. User System Integration

The demo uses **Spring Security** for a simple user system.  

You must provide a `CoWorkUserProvider` implementation to connect GridJs with your user system:

In server-side config [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

For example: here we defined MyCustomUser to implement all the interfaces in CoWorkUserProvider.

```java
@Bean
public CoWorkUserProvider currentUserProvider() {
    return new MyCustomUser();
}
```


I [`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java):

```java
public class MyCustomUser implements CoWorkUserProvider {
    //Get the current login user name
    @Override
    public String getCurrentUserName() {
        return getCurrentUser().getUsername();
    }

    //Get the current login user Id
    @Override
    public Long getCurrentUserId() {
        return getCurrentUser().getUserId();
    }

    //Get the current login user permission
    @Override
    public CoWorkUserPermission getPermission() {
        return CoWorkUserPermission.EDITABLE;
    }

    private static CustomUserDetails getCurrentUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.getPrincipal() instanceof CustomUserDetails) {
            return (CustomUserDetails) authentication.getPrincipal();
        }
        throw new IllegalStateException("User not authenticated");
    }
}
```

---

### 3. WebSocket Configuration

The demo uses **Spring WebSocket** with STOMP.  

Example config:

In [`/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java):

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
        config.setUserDestinationPrefix("/user");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

GridJs förväntar sig att `messageTopic` matchar "/topic/opr" vilket är standard:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

Eller:

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

På klienten:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

Här motsvarar `/GridJs2/msg` ruttvägen definierad i  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java):

```java
@RequestMapping("/GridJs2/msg")
```

#### Exempel med anpassade WebSocket-vägar

Om din server använder en annan konfiguration:

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic_gridjs");
        config.setApplicationDestinationPrefixes("/app_gridjs");
        config.setUserDestinationPrefix("/user_gridjs");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws_gridjs")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

Då måste du ställa in:

**Server-sida**:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

eller

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**Klientsida**:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

detaljdokumentet för setCollaborativeSetting kan hittas [här](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

> ⚠️ Obs: Som standard fungerar demo-konfigurationen direkt.  
Extra konfiguration krävs endast om appen anpassar WebSocket-endpoints.  

Kom ihåg: det kollektiva läget **stödjer inte** lazy loading.  
Aktivera inte `Config.setLazyLoading(true)`.

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## Slutsats

Med Aspose.Cells.GridJs kan du snabbt bygga en kraftfull **samarbetsvillig Excel-redigerare**.  
Kombinationen av Java-backend, GridJs-frontend, SQL-lagring och WebSocket-meddelanden säkerställer tillförlitlig realtidsredigering av kalkylblad.

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
