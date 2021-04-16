// Short term web server on localhost.
package main

import (
	"log"
	"net/http"
)

const ROOT = "."

func main() {
	http.Handle("/", http.FileServer(http.Dir(ROOT)))
	log.Fatal(http.ListenAndServe("localhost:8080", nil))
}
