resource "google_storage_bucket" "auto-expire" {
  name          = "github_action_cicd_create_bjhbskjnabsbisbidb"
  location      = "US"
  force_destroy = true
  project       = "first-project-0768" 
  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}