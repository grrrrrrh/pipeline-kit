package hello

import "testing"

func TestHelloDefault(t *testing.T) {
	if got := Hello(""); got != "Hello, world!" {
		t.Fatalf("expected %q, got %q", "Hello, world!", got)
	}
}

func TestHelloName(t *testing.T) {
	if got := Hello("ND"); got != "Hello, ND!" {
		t.Fatalf("expected %q, got %q", "Hello, ND!", got)
	}
}
