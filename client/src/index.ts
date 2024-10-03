export interface ArtPiece {
  id: number;
  title: string;
  description: string;
  image_path: string;
  author: User;
  upload_date: string;
  tags: Tag[];
  global_rating: number;
}

export interface User {
  id: number;
  username: string;
  email: string;
}

export interface Tag {
  id: number;
  name: string;
}

export interface Review {
  id: number;
  art_piece_id: number;
  user: User;
  rendering_rating: number;
  anatomy_rating: number;
  composition_rating: number;
  rendering_comment?: string;
  anatomy_comment?: string;
  composition_comment?: string;
  global_rating: number;
}
