package main

import ("encoding/json"
	    "flag"
	    "os"
        "github.com/ChimeraCoder/anaconda"
)

func main() {
	handlePtr := flag.String("handle", "TwitterAPI", "Twitter handle")
	anaconda.SetConsumerKey("u1IfrGHbISQOEahLSu1uNHX6U")
	anaconda.SetConsumerSecret("1B2pfbKwwQUo1XJDENy8dXFxtu7e9dkW8MQTSxixNp2epz1C5o")
	api_client := anaconda.NewTwitterApi("1171113971119575040-j9yYMQgautaDZE3vDIlgQ6x7gYf34N ", "SYeDwgctvOOORHFJCbu8eo5a00l0kRIsu9EpDSMWamLGj")
	var user anaconda.User
	user, _ = api_client.GetUsersShow(*handlePtr, nil)
	userJSON, _ := json.MarshalIndent(user, "", " ")
	f, _ := os.Create("./output.txt")
	f.WriteString(string(userJSON))
	f.Sync()
	f.Close()