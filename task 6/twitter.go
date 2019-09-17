package main

import (
    "os"
    "flag"
    "fmt"
    "github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
	
)

func main() {
	var name string    
	fmt.Println("enter the username ")
	fmt.Scanln(&name)
	tn:=flag.String("twitterHandler",name,"it contains the name of twitter handler") 
	flag.Parse()
	config := oauth1.NewConfig("u1IfrGHbISQOEahLSu1uNHX6U", "1B2pfbKwwQUo1XJDENy8dXFxtu7e9dkW8MQTSxixNp2epz1C5o")
	token := oauth1.NewToken("1171113971119575040-j9yYMQgautaDZE3vDIlgQ6x7gYf34N ", "SYeDwgctvOOORHFJCbu8eo5a00l0kRIsu9EpDSMWamLGj")
	httpClient := config.Client(oauth1.NoContext, token)
	client := twitter.NewClient(httpClient)
	f, err := os.Create("userHandler.txt")

	params := &twitter.FollowerListParams{
	        ScreenName: *tn,
	}
    
	followers, resp, err := client.Followers.List(params)
	var count int = 0;
	fmt.Println(resp, err)
	f.WriteString("Followers - " + *tn)
	for _, follower := range followers.Users {
		count=count+1
		f.WriteString("\n" + follower.ScreenName)
	}
	f.WriteString("\n")
	f.WriteString(fmt.Sprintf("\n", count))
    f.Close()}
